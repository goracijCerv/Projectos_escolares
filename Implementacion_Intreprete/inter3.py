import string
import os
import math
import random
#Constantes
DIGITOS = '0123456789'
LETRAS=string.ascii_letters
LETRAS_NUMEROS=LETRAS+DIGITOS
#######################################  
# Errores
class Error:
	def __init__(self, pos_inicio, pos_fin, nom_error, detalles):
		self.pos_inicio = pos_inicio
		self.pos_fin = pos_fin
		self.nom_error = nom_error
		self.detalles = detalles
	
	def as_string(self):
		resultado  = f'{self.nom_error}: {self.detalles}\n'
		resultado += f'Archivo {self.pos_inicio.nom_archivo}, linea {self.pos_inicio.linea + 1}'
		return resultado

class ErrorCaracterIlegal(Error):
	def __init__(self, pos_inicio, pos_fin, detalles):
		super().__init__(pos_inicio, pos_fin, 'Caracter Ilegal', detalles)

class ErrorCaracterEsp(Error):
	def __init__(self, pos_inicio, pos_fin, detalles):
		super().__init__(pos_inicio, pos_fin, 'Se esperaba un caracter', detalles)


class ErrorSintaxis(Error):
	def __init__(self, pos_inicio, pos_fin, detalles=''):
		super().__init__(pos_inicio, pos_fin, 'Sintaxis invalida', detalles)

class ErrorEJ(Error):
	def __init__(self, pos_inicio, pos_fin, detalles, contexto):
		super().__init__(pos_inicio, pos_fin, 'Error de ejecucion', detalles)
		self.contexto = contexto

	def as_string(self):
		resultado  = self.generate_traceback()
		resultado += f'{self.nom_error}: {self.detalles}'
		return resultado

	def generate_traceback(self):
		resultado = ''
		pos = self.pos_inicio
		ctx = self.contexto

		while ctx:
			resultado = f'  Archivo {pos.nom_archivo}, linea {str(pos.linea + 1)}, en {ctx.mostrar_nom}\n' + resultado
			pos = ctx.padre_pos_entrada
			ctx = ctx.padre

		return 'Rastreo (ultima linea):\n' + resultado
#######################################
# Posicion
class Posicion:
	def __init__(self, idx, linea, col, nom_archivo, archivotxt):
		self.idx = idx
		self.linea = linea
		self.col = col
		self.nom_archivo = nom_archivo
		self.archivotxt = archivotxt

	def avanzar(self, caracter_ac=None):
		self.idx += 1
		self.col += 1

		if caracter_ac == '\n':
			self.linea += 1
			self.col = 0

		return self

	def copiar(self):
		return Posicion(self.idx, self.linea, self.col, self.nom_archivo, self.archivotxt)
#######################################
# TOKENS
TT_INT='INT'
TT_FLOAT ='FLOAT'
TT_IDENTIFICADOR='IDENTIFICADOR'
TT_PALABRACLAVE='PALABRACLAVE'
TT_MAS='MAS'
TT_MENOS='MENOS'
TT_MUL='MUL'
TT_DIV='DIV'
TT_POT='POT'
TT_LPAREN='LPAREN'
TT_RPAREN='RPAREN'
TT_LCORCH='LCORCH' #[
TT_RCORCH='RCORCH'#]
TT_IG="IG" #esto es para igual en una vairable
TT_E='E' #esto es equivalente en modo logico (==)
TT_NE='NE' #no equivalente
TT_MEN='MEN'#menor
TT_MAY='MAY'
TT_MENE='MENE'#menor o igual
TT_MAYE='MAYE'
TT_COMA='COMA'
TT_FLC='FLC'#flecha
TT_FA='FA' # final de linea o archivo
TT_CADENA='CADENA'

PALABRACLAVE=[
	'VAR',
	'and',
	'or',
	'NOT',
	'if',
	'else if',
	'else',
	'then',
	'for',
	'to',
	'step',
	'mientras',
	'fun'
]
class Token:
	def __init__(self, tipo_, valor=None, pos_inicio=None, pos_fin=None):
		self.tipo = tipo_
		self.valor = valor

		if pos_inicio:
			self.pos_inicio = pos_inicio.copiar()
			self.pos_fin = pos_inicio.copiar()
			self.pos_fin.avanzar()

		if pos_fin:
			self.pos_fin = pos_fin

	def partido(self, tipo_, valor):
		return self.tipo==tipo_ and self.valor== valor
	
	def __repr__(self):
		if self.valor: return f'{self.tipo}:{self.valor}'
		return f'{self.tipo}'

#######################################
# LEXER
class Lexer:
	def __init__(self, nom_archivo, texto):
		self.nom_archivo = nom_archivo
		self.texto = texto
		self.pos = Posicion(-1, 0, -1, nom_archivo, texto)
		self.caracter_ac = None
		self.avanzar()
	
	def avanzar(self):
		self.pos.avanzar(self.caracter_ac)
		self.caracter_ac = self.texto[self.pos.idx] if self.pos.idx < len(self.texto) else None

	def tokenizar(self):
		tokens = []

		while self.caracter_ac != None:
			if self.caracter_ac in ' \t':
				self.avanzar()
			elif self.caracter_ac in DIGITOS:
				tokens.append(self.hacer_num())
			elif self.caracter_ac in LETRAS:
				tokens.append(self.hacer_identi())
			elif self.caracter_ac == '"':
				tokens.append(self.hacer_cadena())
			elif self.caracter_ac == '+':
				tokens.append(Token(TT_MAS, pos_inicio=self.pos))
				self.avanzar()
			elif self.caracter_ac == '-':
				 tokens.append(self.hacer_menos_flecha())
			elif self.caracter_ac == '*':
				tokens.append(Token(TT_MUL, pos_inicio=self.pos))
				self.avanzar()
			elif self.caracter_ac == '/':
				tokens.append(Token(TT_DIV, pos_inicio=self.pos))
				self.avanzar()
			elif self.caracter_ac == '^':
				tokens.append(Token(TT_POT, pos_inicio=self.pos))
				self.avanzar()
			elif self.caracter_ac == '(':
				tokens.append(Token(TT_LPAREN, pos_inicio=self.pos))
				self.avanzar()
			elif self.caracter_ac == ')':
				tokens.append(Token(TT_RPAREN, pos_inicio=self.pos))
				self.avanzar()
			elif self.caracter_ac == '[':
				tokens.append(Token(TT_LCORCH, pos_inicio=self.pos))
				self.avanzar()
			elif self.caracter_ac == ']':
				tokens.append(Token(TT_RCORCH, pos_inicio=self.pos))
				self.avanzar()
			elif self.caracter_ac == ',':
				tokens.append(Token(TT_COMA, pos_inicio=self.pos))
				self.avanzar()
			elif self.caracter_ac=="!":
				tok,error=self.hacer_no_equi()
				if error: return [],error
				tokens.append(tok)
			elif self.caracter_ac == '=':
				tokens.append(self.hacer_equi())
			elif self.caracter_ac == '<':
				tokens.append(self.hacer_menor())
			elif self.caracter_ac == '>':
				tokens.append(self.hacer_mayor())	
			else:
				pos_inicio = self.pos.copiar()
				char = self.caracter_ac
				self.avanzar()
				return [], ErrorCaracterIlegal(pos_inicio, self.pos, "'" + char + "'")

		tokens.append(Token(TT_FA, pos_inicio=self.pos))
		return tokens, None

	def hacer_num(self):
		num = ''
		bandera = 0
		pos_inicio = self.pos.copiar()

		while self.caracter_ac != None and self.caracter_ac in DIGITOS + '.':
			if self.caracter_ac == '.':
				if bandera == 1: break
				bandera += 1
				num += '.'
			else:
				num += self.caracter_ac
			self.avanzar()

		if bandera == 0:
			return Token(TT_INT, int(num), pos_inicio, self.pos)
		else:
			return Token(TT_FLOAT, float(num), pos_inicio, self.pos)
	
	def hacer_identi(self):
		id=''
		pos_inicio=self.pos.copiar()

		while self.caracter_ac != None and self.caracter_ac in LETRAS_NUMEROS + '_':
			id += self.caracter_ac
			self.avanzar()
		tipo_token=TT_PALABRACLAVE if id in PALABRACLAVE else TT_IDENTIFICADOR
		return Token(tipo_token, id, pos_inicio, self.pos)

	def hacer_no_equi(self):
		pos_inicio=self.pos.copiar()
		self.avanzar() #sabemos que es un ! asi que buscamos que el siguiente sea =

		if self.caracter_ac == '=':
			self.avanzar()
			return Token(TT_NE,pos_inicio=pos_inicio,pos_fin=self.pos),None
		
		self.avanzar()
		return None, ErrorCaracterEsp(pos_inicio,self.pos,"Se esperaba = despues de !")

	def hacer_equi(self):
		tipo_token=TT_IG
		pos_inicio=self.pos.copiar()
		self.avanzar()

		if self.caracter_ac == '=':
			self.avanzar()
			tipo_token=TT_E
		return Token(tipo_token,pos_inicio=pos_inicio,pos_fin=self.pos)	

	def hacer_menor(self):
		tipo_token=TT_MEN
		pos_inicio=self.pos.copiar()
		self.avanzar()

		if self.caracter_ac == '=':
			self.avanzar()
			tipo_token=TT_MENE
		return Token(tipo_token,pos_inicio=pos_inicio,pos_fin=self.pos)	
	
	def hacer_mayor(self):
		tipo_token=TT_MAY
		pos_inicio=self.pos.copiar()
		self.avanzar()

		if self.caracter_ac == '=':
			self.avanzar()
			tipo_token=TT_MAYE
		return Token(tipo_token,pos_inicio=pos_inicio,pos_fin=self.pos)	

	def hacer_menos_flecha(self):
		tipo_token=TT_MENOS
		pos_inicio=self.pos.copiar()
		self.avanzar()
		
		if self.caracter_ac=='>':
			self.avanzar()
			tipo_token=TT_FLC
		return Token(tipo_token,pos_inicio=pos_inicio,pos_fin=self.pos)

	def hacer_cadena(self):
		cadena=''
		pos_inicio=self.pos.copiar()
		bandera=False #es por si se da un enter
		self.avanzar()

		caracteres_de_salto={
			'n':'\n',
			't':'\t'
		}

		while self.caracter_ac != None and (self.caracter_ac != '"' or bandera):
			if bandera:
				cadena += caracteres_de_salto.get(self.caracter_ac, self.caracter_ac)
			else:
				if self.caracter_ac == '\\':
					bandera=True
				else:
					cadena += self.caracter_ac
				self.avanzar()
				bandera=False
		
		self.avanzar()
		return Token(TT_CADENA,cadena,pos_inicio=pos_inicio,pos_fin=self.pos)
			
			

#######################################
# Nodos
class NodoNumero:
	def __init__(self, tok):
		self.tok = tok

		self.pos_inicio = self.tok.pos_inicio
		self.pos_fin = self.tok.pos_fin

	def __repr__(self):
		return f'{self.tok}'

class NodoCadena:
	def __init__(self, tok):
		self.tok = tok

		self.pos_inicio = self.tok.pos_inicio
		self.pos_fin = self.tok.pos_fin

	def __repr__(self):
		return f'{self.tok}'

class NodoADVar:##acces
	def __init__(self,nombre_var_tok):
		self.nombre_var_tok=nombre_var_tok
		
		self.pos_inicio=self.nombre_var_tok.pos_inicio
		self.pos_fin=self.nombre_var_tok.pos_fin

class NodoDVar:##asing
	def __init__(self, nombre_var_tok, valor_nodo):
		self.nombre_var_tok=nombre_var_tok
		self.valor_nodo=valor_nodo

		self.pos_inicio=self.nombre_var_tok.pos_inicio
		self.pos_fin=self.valor_nodo.pos_fin

class NodoOP:
	def __init__(self, nodo_iz, token_op, nodo_der):
		self.nodo_iz = nodo_iz
		self.token_op = token_op
		self.nodo_der = nodo_der

		self.pos_inicio = self.nodo_iz.pos_inicio
		self.pos_fin = self.nodo_der.pos_fin

	def __repr__(self):
		return f'({self.nodo_iz}, {self.token_op}, {self.nodo_der})'

class NodoP:
	def __init__(self, token_op, nodo):
		self.token_op = token_op
		self.nodo = nodo

		self.pos_inicio = self.token_op.pos_inicio
		self.pos_fin = nodo.pos_fin

	def __repr__(self):
		return f'({self.token_op}, {self.nodo})'

class Nodoif:
	def __init__(self,casos,caso_else):
		self.casos=casos
		self.caso_else=caso_else

		self.pos_inicio = self.casos[0][0].pos_inicio
		self.pos_fin = (self.caso_else or self.casos[len(self.casos)-1][0]).pos_fin

class Nodofor:
	def __init__(self,nom_var,valor_var_nodo,valor_fin_nodo,valor_paso_nodo,cuerpo):
		self.nom_var=nom_var
		self.valor_var_nodo=valor_var_nodo
		self.valor_fin_nodo=valor_fin_nodo
		self.valor_paso_nodo=valor_paso_nodo
		self.cuerpo=cuerpo

		self.pos_inicio=self.nom_var.pos_inicio
		self.pos_fin=self.cuerpo.pos_fin

class Nodowhile:
	def __init__(self,condicion_nodo,cuerpo):
		self.condicion_nodo=condicion_nodo
		self.cuerpo=cuerpo

		self.pos_inicio=self.condicion_nodo.pos_inicio
		self.pos_fin=self.cuerpo.pos_fin

class NodoLista:
	def __init__(self,nodos_elementos,pos_inicio,pos_fin):
		self.nodos_elementos=nodos_elementos
		self.pos_inicio=pos_inicio
		self.pos_fin=pos_fin

class Nodofun:
	def __init__(self,nom_fun,nom_args,cuerpro):
		self.nom_fun=nom_fun
		self.nom_args=nom_args
		self.cuerpo=cuerpro

		if self.nom_fun:
			self.pos_inicio= self.nom_fun.pos_inicio
		elif len(self.nom_args) > 0:
			self.pos_inicio=self.nom_args[0].pos_inicio
		else:
			self.pos_inicio=self.cuerpo.pos_inicio
		
		self.pos_fin=self.cuerpo.pos_fin

class Nodollamada:
	def __init__(self,nodo_fun_llamar,nodos_args):
		self.nodo_fun_llamar=nodo_fun_llamar
		self.nodos_args=nodos_args
		self.pos_inicio=self.nodo_fun_llamar.pos_inicio

		if len(nodos_args) > 0 :
			self.pos_fin=self.nodos_args[len(self.nodos_args)-1].pos_fin
		else:
			self.pos_fin=self.nodo_fun_llamar.pos_fin


#######################################
# Resultado del parser
class ParsenResultado:
	def __init__(self):
		self.error = None
		self.nodo = None
		self.cont_avance=0
    
	def registro_avance(self):
		self.cont_avance +=1

	def registro(self, res):
		self.cont_avance += res.cont_avance
		if res.error: self.error = res.error
		return res.nodo


	def exito(self, nodo):
		self.nodo = nodo
		return self

	def fallo(self, error):
		if not self.error or self.cont_avance == 0:
			self.error = error
		return self

#######################################
# PARSER
class Parser:
	def __init__(self, tokens):
		self.tokens = tokens
		self.tok_idx = -1
		self.avanzar()

	def avanzar(self, ):
		self.tok_idx += 1
		if self.tok_idx < len(self.tokens):
			self.token_act = self.tokens[self.tok_idx]
		return self.token_act

	def parse(self):
		res = self.expr()
		if not res.error and self.token_act.tipo != TT_FA:
			return res.fallo(ErrorSintaxis(self.token_act.pos_inicio, self.token_act.pos_fin,"Se esperaba '+', '-', '*', '/'"))
		return res

	#############Estructura gramatical################

	def atom(self):
		res = ParsenResultado()
		tok = self.token_act

		if tok.tipo in (TT_INT, TT_FLOAT):
			res.registro_avance()
			self.avanzar()
			return res.exito(NodoNumero(tok))

		elif tok.tipo == TT_CADENA:
			res.registro_avance()
			self.avanzar()
			return res.exito(NodoCadena(tok))

		elif tok.tipo==TT_IDENTIFICADOR:
			res.registro_avance()
			self.avanzar()
			return res.exito(NodoADVar(tok))

		elif tok.tipo == TT_LPAREN:
			res.registro_avance()
			self.avanzar()
			expr = res.registro(self.expr())
			if res.error: return res
			if self.token_act.tipo == TT_RPAREN:
				res.registro_avance()
				self.avanzar()
				return res.exito(expr)
			else:
				return res.fallo(ErrorSintaxis(self.token_act.pos_inicio, self.token_act.pos_fin,"Se esperaba ')'"))
		
		elif tok.tipo== TT_LCORCH:
			lista_def=res.registro(self.defini_lista())
			if res.error: return res
			return res.exito(lista_def)
			 

		elif tok.partido(TT_PALABRACLAVE,'if'):
			expr_if=res.registro(self.expr_if())
			if res.error: return res
			return res.exito(expr_if)
		
		elif tok.partido(TT_PALABRACLAVE,'for'):
			expr_for=res.registro(self.expr_for())
			if res.error: return res
			return res.exito(expr_for)  

		elif tok.partido(TT_PALABRACLAVE,'mientras'):
			expr_while=res.registro(self.expr_while())
			if res.error: return res
			return res.exito(expr_while) 	
		
		elif tok.partido(TT_PALABRACLAVE,'fun'):
			defini_fun=res.registro(self.defini_fun())
			if res.error: return res
			return res.exito(defini_fun) 	

		return res.fallo(ErrorSintaxis(tok.pos_inicio, tok.pos_fin,"Se esperaba INT, FLOAT, identificador, '+', '-', '(','[', for, if, mientras, fun"))

	def power(self):
		return self.bin_op(self.llamada, (TT_POT, ), self.factor)

	def llamada(self):
		res=ParsenResultado()
		atomo=res.registro(self.atom())
		if res.error: return res
		
		if self.token_act.tipo == TT_LPAREN:
			res.registro_avance()
			self.avanzar()
			nodos_argu=[]
			
			if self.token_act.tipo == TT_RPAREN:
				res.registro_avance()
				self.avanzar()
			else:
				nodos_argu.append(res.registro(self.expr()))
				if res.error:
					return res.fallo(ErrorSintaxis(
						self.token_act.pos_inicio,self.token_act.pos_fin,
					    f"Se esperaba VAR, if, for, mientras, fun, INT, FLOAT, identificador, '+' , '-' ,'(', '[' o NOT "))
				while self.token_act.tipo== TT_COMA:
					res.registro_avance()
					self.avanzar()
					nodos_argu.append(res.registro(self.expr()))
					if res.error: return res
					
				if self.token_act.tipo != TT_RPAREN:
					return res.fallo(ErrorSintaxis(
					self.token_act.pos_inicio,self.token_act.pos_fin,
				    f'Se esperaba una , o )' ))
				
				res.registro_avance()
				self.avanzar()
			return res.exito(Nodollamada(atomo,nodos_argu))

		return res.exito(atomo)


	def factor(self):
		res = ParsenResultado()
		tok = self.token_act

		if tok.tipo in (TT_MAS, TT_MENOS):
			res.registro_avance()
			self.avanzar()
			factor = res.registro(self.factor())
			if res.error: return res
			return res.exito(NodoP(tok, factor))

		return self.power()

	def term(self):
		return self.bin_op(self.factor, (TT_MUL, TT_DIV))

	def expr_arit(self):
		return self.bin_op(self.term, (TT_MAS,TT_MEN))
	
	def expr_com(self):
		res=ParsenResultado()
		
		if self.token_act.partido(TT_PALABRACLAVE, 'NOT'):
			token_op=self.token_act
			res.registro_avance()
			self.avanzar()
			nodo=res.registro(self.expr_com())
			if res.error: return res
			return res.exito(NodoP(token_op,nodo))
		
		nodo=res.registro(self.bin_op(self.expr_arit,(TT_E,TT_NE,TT_MEN,TT_MAY,TT_MENE,TT_MAYE)))
		if res.error:
			return res.fallo(ErrorSintaxis(
				self.token_act.pos_inicio,self.token_act.pos_fin, 
				"Se esperaba INT, FLOAT, identificador, '+', '-', '(','[' , NOT"
			))

		return res.exito(nodo)

	def defini_lista(self):
		res=ParsenResultado()
		elementos=[]
		pos_inicio=self.token_act.pos_inicio.copiar()
		

		if self.token_act.tipo != TT_LCORCH:
			res.fallo(ErrorSintaxis(
				self.token_act.pos_inicio,self.token_act.pos_fin,
				f'Se esperaba ['))
		
		res.registro_avance()
		self.avanzar()

		if self.token_act.tipo == TT_RCORCH:
			res.registro_avance()
			self.avanzar()
		else:
			elementos.append(res.registro(self.expr()))
			if res.error:
				return res.fallo(ErrorSintaxis(
				self.token_act.pos_inicio,self.token_act.pos_fin,
				f"Se esperaba ']', VAR, if, for, mientras, fun, INT, FLOAT, identificador, '+' , '-' , '(', '[' "))
			while self.token_act.tipo== TT_COMA:
				res.registro_avance()
				self.avanzar()
				elementos.append(res.registro(self.expr()))
				if res.error: return res
					
			if self.token_act.tipo != TT_RCORCH:
				return res.fallo(ErrorSintaxis(
				self.token_act.pos_incio,self.token_act.pos_fin,
				f'Se esperaba una , o ]' ))
			
			res.registro_avance()
			self.avanzar()
				
		return res.exito(NodoLista(elementos,pos_inicio,self.token_act.pos_fin.copiar()))


	def expr_if(self):
		res=ParsenResultado()
		casos=[]
		caso_else=None

		if not self.token_act.partido(TT_PALABRACLAVE,'if'):
			return res.fallo(ErrorSintaxis(
				self.token_act.pos_incio,self.token_act.pos_fin,
				'Se esperaba if'))
		
		res.registro_avance()
		self.avanzar()
		condicion= res.registro(self.expr())
		if res.error: return res

		if not self.token_act.partido(TT_PALABRACLAVE,'then'):
			return res.fallo(ErrorSintaxis(
				self.token_act.pos_inicio,self.token_act.pos_fin,
				'Se esperaba then'))
		
		res.registro_avance()
		self.avanzar()
		expr=res.registro(self.expr())
		if res.error: return res
		casos.append((condicion,expr))

		while self.token_act.partido(TT_PALABRACLAVE,'else if'):
			res.registro_avance()
			self.avanzar()
			condicion=res.registro(self.expr())
			if res.error: return res

			if not self.token_act.partido(TT_PALABRACLAVE,'then'):
				return res.fallo(ErrorSintaxis(
					self.token_act.pos_inicio,self.token_act.pos_fin,
					'Se esperaba then'))
			
			res.registro_avance()
			self.avanzar()
			expr=res.registro(self.expr())
			if res.error: return res
			casos.append((condicion,expr))

		if self.token_act.partido(TT_PALABRACLAVE,'else'):
			res.registro_avance()
			self.avanzar()
			caso_else= res.registro(self.expr())
			if res.error: return res
			
		return res.exito(Nodoif(casos,caso_else))

	def expr_for(self):
		res=ParsenResultado()

		if not self.token_act.partido(TT_PALABRACLAVE,'for'):
			return res.fallo(ErrorSintaxis(
				self.token_act.pos_incio,self.token_act.pos_fin,
				'Se esperaba for'))
		
		res.registro_avance()
		self.avanzar()
		
		if self.token_act.tipo != TT_IDENTIFICADOR:
			return res.fallo(ErrorSintaxis(
				self.token_act.pos_inicio,self.token_act.pos_fin,
				'Se esperaba un identificador'))
		
		nom_var=self.token_act
		res.registro_avance()
		self.avanzar()
		
		if self.token_act.tipo != TT_IG:
			return res.fallo(ErrorSintaxis(
				self.token_act.pos_inicio,self.token_act.pos_fin,
                "Se esperaba un ="))
		
		res.registro_avance()
		self.avanzar()
		valor_inicial=res.registro(self.expr())
		if res.error: return res

		if not self.token_act.partido(TT_PALABRACLAVE,'to'):
			return res.fallo(ErrorSintaxis(
				self.token_act.pos_inicio,self.token_act.pos_fin,
				"Se esperaba to"))
		
		res.registro_avance()
		self.avanzar()
		valor_fin=res.registro(self.expr())
		if res.error: return res

		if self.token_act.partido(TT_PALABRACLAVE,'step'):
			res.registro_avance()
			self.avanzar()
			caso_step=res.registro(self.expr())
			if res.error: return res
		else:
			caso_step=None

		if not self.token_act.partido(TT_PALABRACLAVE,'then'):
			return res.fallo(ErrorSintaxis(
				self.token_act.pos_inicio,self.token_act.pos_fin,
			    "Se esperaba then"))
		
		res.registro_avance()
		self.avanzar()
		cuerpo=res.registro(self.expr())
		if res.error: return res
		return res.exito(Nodofor(nom_var,valor_inicial,valor_fin,caso_step,cuerpo))

	def expr_while(self):
		res=ParsenResultado()

		if not self.token_act.partido(TT_PALABRACLAVE,'mientras'):
			return res.fallo(ErrorSintaxis(
				self.token_act.pos_inicio,self.token_act.pos_fin,
			    "Se esperaba mientras"))
		res.registro_avance()
		self.avanzar()
		condicion=res.registro(self.expr())
		if res.error: return res
        
		if not self.token_act.partido(TT_PALABRACLAVE,'then'):
			return res.fallo(ErrorSintaxis(
				self.token_act.pos_inicio,self.token_act.pos_fin,
			    "Se esperaba then"))
		res.registro_avance()
		self.avanzar()
		cuerpo=res.registro(self.expr())
		if res.error: return res
		return res.exito(Nodowhile(condicion,cuerpo))

	def defini_fun(self):
		res=ParsenResultado()
		if not self.token_act.partido(TT_PALABRACLAVE,'fun'):
			return res.fallo(ErrorSintaxis(
				self.token_act.pos_inicio,self.token_act.pos_fin,
			    f"Se esperaba fun"))
		
		res.registro_avance()
		self.avanzar()

		if self.token_act.tipo == TT_IDENTIFICADOR:
			nombre=self.token_act
			res.registro_avance()
			self.avanzar()
			if self.token_act.tipo != TT_LPAREN:
				return res.fallo(ErrorSintaxis(
					self.token_act.pos_inicio,self.token_act.pos_fin,
				    'Se esperaba un ('))
		else:
			nombre=None
			if self.token_act.tipo != TT_LPAREN:
				return res.fallo(ErrorSintaxis(
					self.token_act.pos_inicio,self.token_act.pos_fin,
				    f'Se esperaba un ('))
		
		res.registro_avance()
		self.avanzar()
		tokens_arg=[]

		if self.token_act.tipo == TT_IDENTIFICADOR:
			tokens_arg.append(self.token_act)
			res.registro_avance()
			self.avanzar()

			while self.token_act.tipo == TT_COMA:
				res.registro_avance()
				self.avanzar()

				if self.token_act.tipo != TT_IDENTIFICADOR:
					return res.fallo(ErrorSintaxis(
						self.token_act.pos_inicio,self.token_act.pos_fin,
					    f"Se esperaba un identificador"))
				
				tokens_arg.append(self.token_act)
				res.registro_avance()
				self.avanzar()
			if self.token_act.tipo != TT_RPAREN:
				return res.fallo(ErrorSintaxis(
					self.token_act.pos_incio,self.token_act.pos_fin,
				    f'Se esperaba una , o )' ))
		else:
			if self.token_act.tipo != TT_RPAREN:
				return res.fallo(ErrorSintaxis(
					self.token_act.pos_incio, self.token_act.pos_fin,
					f'Se esperaba un identificador o )'))
		
		res.registro_avance()
		self.avanzar()
		if self.token_act.tipo != TT_FLC:
			return res.fallo(ErrorSintaxis(
				self.token_act.pos_inicio, self.token_act.pos_fin,
				f'Se esperaba ->'))
		
		res.registro_avance()
		self.avanzar()
		retornar=res.registro(self.expr())
		if res.error: return res
		return res.exito(Nodofun(nombre,tokens_arg,retornar))

	def expr(self):
		res=ParsenResultado()

		if self.token_act.partido(TT_PALABRACLAVE, 'VAR'):
			res.registro_avance()
			self.avanzar()

			if self.token_act.tipo != TT_IDENTIFICADOR:
				return res.fallo(ErrorSintaxis(self.token_act.pos_inicio, self.token_act.pos_fin,"Se esperaba un identificador"))
			nombre_var=self.token_act
			res.registro_avance()
			self.avanzar()

			if self.token_act.tipo != TT_IG:
				return res.fallo(ErrorSintaxis(self.token_act.pos_inicio, self.token_act.pos_fin,"Se esperaba un ="))
			res.registro_avance()
			self.avanzar()
			exp=res.registro(self.expr())
			if res.error: return res
			return res.exito(NodoDVar(nombre_var,exp)) 	

		nodo=res.registro(self.bin_op(self.expr_com, ((TT_PALABRACLAVE,'and'),(TT_PALABRACLAVE,'or'))))
		if res.error:
			return res.fallo(ErrorSintaxis(self.token_act.pos_inicio,self.token_act.pos_fin,
			"Se esperaba VAR, int, float, identificador, for, if, mientras, fun, '+' , '-' , '(', '[' o NOT"))
		return res.exito(nodo)

	###################################

	def bin_op(self, func_a, ops, func_b=None):
		if func_b == None:
			func_b = func_a
		
		res = ParsenResultado()
		left = res.registro(func_a())
		if res.error: return res

		while self.token_act.tipo in ops or (self.token_act.tipo, self.token_act.valor) in ops:
			token_op = self.token_act
			res.registro_avance()
			self.avanzar()
			right = res.registro(func_b())
			if res.error: return res
			left = NodoOP(left, token_op, right)

		return res.exito(left)

#######################################
# Resultado de la Ejecuicon
class ResultadoEJ:
	def __init__(self):
		self.valor = None
		self.error = None

	def registro(self, res):
		if res.error: self.error = res.error
		return res.valor

	def exito(self, valor):
		self.valor = valor
		return self

	def fallo(self, error):
		self.error = error
		return self

#######################################
# Almacen de los valores
class Valor:
	def __init__(self):
		self.poner_pos()
		self.poner_contexto()
	
	def poner_pos(self, pos_inicio=None, pos_fin=None):
		self.pos_inicio = pos_inicio
		self.pos_fin = pos_fin
		return self

	def poner_contexto(self, contexto=None):
		self.contexto = contexto
		return self
    
	def sumar_a(self, otro):
		return None, self.operacion_ilegal(otro)

	def restar_a(self, otro):
		return None, self.operacion_ilegal(otro)
	
	def mutiplicar_a(self, otro):
		return None, self.operacion_ilegal(otro)
		
	def dividir_a(self, otro):
		return None, self.operacion_ilegal(otro)

	def potenciar_por(self, otro):
		return None, self.operacion_ilegal(otro)

	def obt_comp_equi(self,otro):
		return None, self.operacion_ilegal(otro)

	def obt_comp_no_equi(self,otro):
		return None, self.operacion_ilegal(otro)
    
	def obt_comp_menor(self,otro):
		return None, self.operacion_ilegal(otro)

	def obt_comp_mayor(self,otro):
		return None, self.operacion_ilegal(otro)

	def obt_comp_menor_equi(self,otro):
		return None, self.operacion_ilegal(otro)

	def obt_comp_mayor_equi(self,otro):
		return None, self.operacion_ilegal(otro)

	def operacion_and(self,otro):
		return None, self.operacion_ilegal(otro)

	def operacion_or(self,otro):
		return None, self.operacion_ilegal(otro)

	def noad(self):
		return None, self.operacion_ilegal()

	def is_true(self):
		return False

	def ejecutar(self, argumetentos):
		return None, self.operacion_ilegal()

	def copiar(self):
		raise Exception("No esta definido el metodo copiar")

	def operacion_ilegal(self, otro=None):
		if not otro: otro=self
		return ErrorEJ(
			self.pos_inicio,otro.pos_fin,
			f'Operacion ilegal',self.contexto
		)

class Numero(Valor):
	def __init__(self, valor):
		super().__init__()
		self.valor = valor

	def sumar_a(self, otro):
		if isinstance(otro, Numero):
			return Numero(self.valor + otro.valor).poner_contexto(self.contexto), None
		else: 
			return None,Valor.operacion_ilegal(self.pos_inicio, otro.pos_fin)

	def restar_a(self, otro):
		if isinstance(otro, Numero):
			return Numero(self.valor - otro.valor).poner_contexto(self.contexto), None
		else: 
			return None,Valor.operacion_ilegal(self.pos_inicio, otro.pos_fin)

	def mutiplicar_a(self, otro):
		if isinstance(otro, Numero):
			return Numero(self.valor * otro.valor).poner_contexto(self.contexto), None
		else: 
			return None,Valor.operacion_ilegal(self.pos_inicio, otro.pos_fin)

	def dividir_a(self, otro):
		if isinstance(otro, Numero):
			if otro.valor == 0:
				return None, ErrorEJ(
					otro.pos_inicio, otro.pos_fin,
					'Division de cero',
					self.contexto
				)

			return Numero(self.valor / otro.valor).poner_contexto(self.contexto), None
		else: 
			return None,Valor.operacion_ilegal(self.pos_inicio, otro.pos_fin)

	def potenciar_por(self, otro):
		if isinstance(otro, Numero):
			return Numero(self.valor ** otro.valor).poner_contexto(self.contexto), None
		else: 
			return None,Valor.operacion_ilegal(self.pos_inicio, otro.pos_fin)

	def obt_comp_equi(self,otro):
		if isinstance(otro, Numero):
			return Numero(int(self.valor == otro.valor)).poner_contexto(self.contexto), None
		else: 
			return None,Valor.operacion_ilegal(self.pos_inicio, otro.pos_fin)

	def obt_comp_no_equi(self,otro):
		if isinstance(otro, Numero):
			return Numero(int(self.valor != otro.valor)).poner_contexto(self.contexto), None
		else: 
			return None,Valor.operacion_ilegal(self.pos_inicio, otro.pos_fin)
    
	def obt_comp_menor(self,otro):
		if isinstance(otro, Numero):
			return Numero(int(self.valor < otro.valor)).poner_contexto(self.contexto), None
		else: 
			return None,Valor.operacion_ilegal(self.pos_inicio, otro.pos_fin)

	def obt_comp_mayor(self,otro):
		if isinstance(otro, Numero):
			return Numero(int(self.valor > otro.valor)).poner_contexto(self.contexto), None
		else: 
			return None,Valor.operacion_ilegal(self.pos_inicio, otro.pos_fin)

	def obt_comp_menor_equi(self,otro):
		if isinstance(otro, Numero):
			return Numero(int(self.valor <= otro.valor)).poner_contexto(self.contexto), None
		else: 
			return None,Valor.operacion_ilegal(self.pos_inicio, otro.pos_fin)

	def obt_comp_mayor_equi(self,otro):
		if isinstance(otro, Numero):
			return Numero(int(self.valor >= otro.valor)).poner_contexto(self.contexto), None
		else: 
			return None,Valor.operacion_ilegal(self.pos_inicio, otro.pos_fin)

	def operacion_and(self,otro):
		if isinstance(otro, Numero):
			return Numero(int(self.valor and otro.valor)).poner_contexto(self.contexto), None
		else: 
			return None,Valor.operacion_ilegal(self.pos_inicio, otro.pos_fin)

	def operacion_or(self,otro):
		if isinstance(otro, Numero):
			return Numero(int(self.valor or otro.valor)).poner_contexto(self.contexto), None
		else: 
			return None,Valor.operacion_ilegal(self.pos_inicio, otro.pos_fin)

	def noad(self):
		return Numero(1 if self.valor == 0 else 0).poner_contexto(self.contexto),None

	def is_true(self):
		return self.valor != 0

	def copiar(self):
		copia=Numero(self.valor)
		copia.poner_pos(self.pos_inicio,self.pos_fin)
		copia.poner_contexto(self.contexto)
		return copia

	def __repr__(self):
		return str(self.valor)
Numero.null=Numero(0)
Numero.falso=Numero(0)
Numero.verdadero=Numero(1)
Numero.pi=Numero(math.pi)
############################################
class Cadena(Valor):
	def __init__(self, valor):
		super().__init__()
		self.valor=valor

	def sumar_a(self ,otro):
		if isinstance(otro, Cadena):
			return Cadena(self.valor + otro.valor).poner_contexto(self.contexto), None
		else: 
			return None,Valor.operacion_ilegal(self, otro)
	
	def mutiplicar_a(self ,otro):
		if isinstance(otro, Numero):
			return Cadena(self.valor * otro.valor).poner_contexto(self.contexto), None
		else: 
			return None,Valor.operacion_ilegal(self, otro)
    
	def is_true(self):
		return len(self.valor) > 0

	def copiar(self):
		copia=Cadena(self.valor)
		copia.poner_pos(self.pos_inicio,self.pos_fin)
		copia.poner_contexto(self.contexto)
		return copia

	def __str__(self):
		return self.valor

	def __repr__(self):
		return f'"{self.valor}"'

class Lista(Valor):
	def __init__(self,elementos):
		super().__init__()
		self.elementos=elementos

	def sumar_a(self ,otro): #añade cualquier elmento no nos importa, puede ser int float, lista funcion lo que sea
		lista_tem=self.copiar()
		lista_tem.elementos.append(otro)
		return lista_tem, None

	def restar_a(self,otro): #eliminar el indice de la lista
		if isinstance(otro,Numero): #debe ser un numero por que este es un idice 
			lista_tem=self.copiar()
			try:
				lista_tem.elementos.pop(otro.valor)
				return lista_tem,None
			except:
				return None,ErrorEJ(otro.pos_inicio, otro.pos_fin,
				f"El eleemento de este indice no puede ser removido porque el indice esta fuera de los limites de la lista(vector)",
				self.contexto)
		else:
			return None,Valor.operacion_ilegal(self, otro)

	def mutiplicar_a(self ,otro): #junta las dos listas
		if isinstance(otro, Lista):
			lista_tem=self.copiar()
			lista_tem.elementos.extend(otro.elementos) ##el metodo extend de pyhton concadena dos listas
			return lista_tem,None
		else: 
			return None,Valor.operacion_ilegal(self, otro)

	def dividir_a(self,otro): ##retorna el elelento del indice establecido
		if isinstance(otro,Numero): #debe ser un numero por que este es un idice 
			try:
				return self.elementos[otro.valor], None
			except:
				return None,ErrorEJ(otro.pos_inicio, otro.pos_fin,
				f"El eleemento de este indice no puede ser encontrado porque el indice esta fuera de los limites de la lista(vector)",
				self.contexto)
		else:
			return None,Valor.operacion_ilegal(self, otro)

	def copiar(self):
		copia=Lista(self.elementos)
		copia.poner_pos(self.pos_inicio,self.pos_fin)
		copia.poner_contexto(self.contexto)
		return copia

	def __str__(self):
		return ", ".join([str(x) for x in self.elementos])


	def __repr__(self):
		return f'[{", ".join([str(x) for x in self.elementos])}]'

class Funcion_base(Valor):
	def __init__(self,nombre):
		super().__init__()
		self.nombre= nombre or "anonima"
		
	def nuevo_contexto(self):
		nuev_con=Contexto(self.nombre, self.contexto, self.pos_inicio)
		nuev_con.tabla_sim=Tablasim(nuev_con.padre.tabla_sim)
		return nuev_con

	def comp_arg(self, nom_args,args):
		res =ResultadoEJ()
		if len(args) < len(nom_args):
			return res.fallo(ErrorEJ(
				self.pos_inicio,self.pos_fin,
				f'la cantidad de argumentos es menor a la establecida en {self.nombre}',
				self.contexto))
		elif len(args) > len(nom_args):
			return res.fallo(ErrorEJ(
				self.pos_inicio,self.pos_fin,
				f'la cantidad de argumentos es mayor a la establecida en {self.nombre}',
				self.contexto))
		return res.exito(None)

	def calcular_arg(self, nom_args,args,contexto):
		for i in range(len(args)):
			nom_arg=nom_args[i]
			valor_arg=args[i]
			valor_arg.poner_contexto(contexto)
			contexto.tabla_sim.set(nom_arg,valor_arg)

	def com_cal(self,nom_args,args,contexto):
		res=ResultadoEJ()
		res.registro(self.comp_arg(nom_args,args))
		if res.error: return res
		self.calcular_arg(nom_args,args,contexto)
		return res.exito(None)


class Funcion(Funcion_base):
	def __init__(self,nombre,cuerpo,nodos_arg):
		super().__init__(nombre)
		self.cuerpo=cuerpo
		self.nodos_arg=nodos_arg
	
	def ejecutar(self,parametros):##se llamara cada vez que se quiera ejecutar la funcion 
		res = ResultadoEJ()
		nuev_inter = Interpreter()
		contexto_eje=self.nuevo_contexto()
		#verificando que la cantidad de argumentos esten correctos
		res.registro(self.com_cal(self.nodos_arg,parametros,contexto_eje))
		if res.error: return res

		valor= res.registro(nuev_inter.visitar(self.cuerpo,contexto_eje))
		if res.error: return res
		return res.exito(valor)
	
	def copiar(self):
		copia=Funcion(self.nombre,self.cuerpo,self.nodos_arg)
		copia.poner_pos(self.pos_inicio,self.pos_fin)
		copia.poner_contexto(self.contexto)
		return copia

	def __repr__(self):
		return f'<funcion {self.nombre}>'

class Funcion_inter(Funcion_base):
	def __init__(self, nombre):
		super().__init__(nombre)
	
	def ejecutar(self, argumetentos):
		res = ResultadoEJ()
		contexto_eje=self.nuevo_contexto()
		nombre_fun=f'ejecutar_{self.nombre}'
		fun=getattr(self,nombre_fun,self.no_ejecutar)
		res.registro(self.com_cal(fun.nodos_arg,argumetentos,contexto_eje))
		if res.error: return res

		valor_retorn=res.registro(fun(contexto_eje))
		if res.error: return res
		return res.exito(valor_retorn)
	
	def no_ejecutar(self,node,contexto):
		raise Exception(f'No se a ejecutado {self.nombre} dado que su ejecucion no esta definida')

	def copiar(self):
		copia=Funcion_inter(self.nombre)
		copia.poner_pos(self.pos_inicio,self.pos_fin)
		copia.poner_contexto(self.contexto)
		return copia

	def __repr__(self):
		return f'<funcion prestablecida {self.nombre}>'
    #####################################################

	def ejecutar_print(self, contexto_eje):
		print(str(contexto_eje.tabla_sim.get("valor")))
		return ResultadoEJ().exito(Numero.null)
	ejecutar_print.nodos_arg=["valor"]

	def ejecutar_print_ret(self, contexto_eje):
		return ResultadoEJ().exito(Cadena(str(contexto_eje.tabla_sim.get("valor"))))
	ejecutar_print_ret.nodos_arg=["valor"]

	def ejecutar_input(self,contexto_eje): ##es para recibir entradas del teclado
		texto= input()
		return ResultadoEJ().exito(Cadena(texto))
	ejecutar_input.nodos_arg=[]

	def ejecutar_input_int(self,contexto_eje): #recibe numeros
		while True:
			texto= input()
			try:
				numero=int(texto)
				break
			except ValueError:
				print(f'{texto} debe ser un numero entero, vuelve a intentarlo')
		return ResultadoEJ().exito(Numero(numero))
	ejecutar_input_int.nodos_arg=[]

	def ejecutar_limpiar(self, contexto_eje):
		os.system('cls' if os.name == 'nt' else 'clear')
		return ResultadoEJ().exito(Numero.null)
	ejecutar_limpiar.nodos_arg=[]

	def ejecutar_es_numero(self,contexto_eje):
		es_numero=isinstance(contexto_eje.tabla_sim.get('valor'),Numero)
		return ResultadoEJ().exito(Numero.verdadero if es_numero else  Numero.falso)
	ejecutar_es_numero.nodos_arg=['valor']
			
	def ejecutar_es_cadena(self,contexto_eje):
		es_numero=isinstance(contexto_eje.tabla_sim.get('valor'),Cadena)
		return ResultadoEJ().exito(Numero.verdadero if es_numero else  Numero.falso)
	ejecutar_es_cadena.nodos_arg=['valor']

	def ejecutar_es_lista(self,contexto_eje):
		es_numero=isinstance(contexto_eje.tabla_sim.get('valor'),Lista)
		return ResultadoEJ().exito(Numero.verdadero if es_numero else  Numero.falso)
	ejecutar_es_lista.nodos_arg=['valor']

	def ejecutar_es_funcion(self,contexto_eje):
		es_numero=isinstance(contexto_eje.tabla_sim.get('valor'),Funcion_base) #se usa funcion base por que podria ser una funcion interna o una funcion de usario
		return ResultadoEJ().exito(Numero.verdadero if es_numero else  Numero.falso)
	ejecutar_es_funcion.nodos_arg=['valor']

	def ejecutar_agregar(self,contexto_eje):
		lista=contexto_eje.tabla_sim.get('lista')
		valor=contexto_eje.tabla_sim.get('valor')
		if  not isinstance(lista, Lista):
			return ResultadoEJ().fallo(ErrorEJ(
				self.pos_inicio,self.pos_fin,
				"El primer argumento debe ser una lista",
				contexto_eje))
		
		lista.elementos.append(valor)
		return ResultadoEJ().exito(Numero.null)
	ejecutar_agregar.nodos_arg=['lista', 'valor']

	def ejecutar_pop(self,contexto_eje):
		lista=contexto_eje.tabla_sim.get('lista')
		indice=contexto_eje.tabla_sim.get('indice')
		if  not isinstance(lista, Lista):
			return ResultadoEJ().fallo(ErrorEJ(
				self.pos_inicio,self.pos_fin,
				"El primer argumento debe ser una lista",
				contexto_eje))
		
		if  not isinstance(indice, Numero):
			return ResultadoEJ().fallo(ErrorEJ(
				self.pos_inicio,self.pos_fin,
				"El segundo argumento debe ser un numero",
				contexto_eje))
		
		try:
			elemento=lista.elementos.pop(indice.valor)
		except:
			return ErrorEJ(self.pos_inicio, self.pos_fin,
				f"El eleemento de este indice no puede ser removido porque el indice esta fuera de los limites de la lista(vector)",
				contexto_eje)
		return ResultadoEJ().exito(elemento)
	ejecutar_pop.nodos_arg=['lista','indice'] #establece los nombres de los argumentos

	def ejecutar_conca(self,contexto_eje):
		listA=contexto_eje.tabla_sim.get('lista1')
		listB=contexto_eje.tabla_sim.get('lista2')

		if  not isinstance(listA, Lista):
			return ResultadoEJ().fallo(ErrorEJ(
				self.pos_inicio,self.pos_fin,
				"El primer argumento debe ser una lista",
				contexto_eje))
		
		if  not isinstance(listB, Lista):
			return ResultadoEJ().fallo(ErrorEJ(
				self.pos_inicio,self.pos_fin,
				"El segundo argumento debe ser una lista",
				contexto_eje))

		listA.elementos.extend(listB.elementos)
		return ResultadoEJ().exito(Numero.null)
	ejecutar_conca.nodos_arg=['lista1','lista2']

	def ejecutar_sqrt(self, contexto_eje):
		numero=contexto_eje.tabla_sim.get('valor')
		if  not isinstance(numero, Numero):
			return ResultadoEJ().fallo(ErrorEJ(
				self.pos_inicio,self.pos_fin,
				"El argumento debe ser un numero",
				contexto_eje))
		
		resultado=math.sqrt(numero.valor)
		return ResultadoEJ().exito(Numero(resultado))
	ejecutar_sqrt.nodos_arg=['valor']

	def ejecutar_aleatorio_ent(self,contexto_eje):
		liminfe=contexto_eje.tabla_sim.get('num1')
		limsup=contexto_eje.tabla_sim.get('num2')

		if  not isinstance(liminfe, Numero):
			return ResultadoEJ().fallo(ErrorEJ(
				self.pos_inicio,self.pos_fin,
				"El primer argumento debe ser un numero enterp",
				contexto_eje))
		
		if  not isinstance(limsup, Numero):
			return ResultadoEJ().fallo(ErrorEJ(
				self.pos_inicio,self.pos_fin,
				"El segundo argumento debe ser una numero entero",
				contexto_eje))

		numero_al=random.randint(liminfe.valor,limsup.valor)
		return ResultadoEJ().exito(Numero(numero_al))
	ejecutar_aleatorio_ent.nodos_arg=['num1','num2']

##se asigan costantes para las funciones contruidas
Funcion_inter.print=Funcion_inter("print")
Funcion_inter.print_ret=Funcion_inter("print_ret")
Funcion_inter.input=Funcion_inter("input")
Funcion_inter.input_int=Funcion_inter("input_int")
Funcion_inter.limpiar=Funcion_inter("limpiar")
Funcion_inter.es_numero=Funcion_inter("es_numero")
Funcion_inter.es_cadena=Funcion_inter("es_cadena")
Funcion_inter.es_funcion=Funcion_inter("es_funcion")
Funcion_inter.es_lista=Funcion_inter("es_lista")
Funcion_inter.agregar=Funcion_inter("agregar")
Funcion_inter.pop=Funcion_inter("pop")
Funcion_inter.conca=Funcion_inter("conca")
Funcion_inter.sqrt=Funcion_inter("sqrt")
Funcion_inter.aleatorio_ent=Funcion_inter('aleatorio_ent')
#######################################
# Contexto
class Contexto:
	def __init__(self, mostrar_nom, padre=None, padre_pos_entrada=None):
		self.mostrar_nom = mostrar_nom
		self.padre = padre
		self.padre_pos_entrada = padre_pos_entrada
		self.tabla_sim=None

#######################################
#Tabla de simbolos
class Tablasim:
	def __init__(self,padre=None):
		self.simbolos={} #almacena las variables
		self.padre=padre

	def get(self, nom):
		valor=self.simbolos.get(nom,None)
		if valor==None and self.padre:
			return self.padre.get(nom)
		return valor
    
	def set(self,nom,valor):
		self.simbolos[nom]=valor

	def remover(self,nom):
		del self.simbolos[nom]

#######################################
# interprete(lee lo que deja el parser)
class Interpreter:
	def visitar(self, nodo, contexto):
		method_name = f'visitar_{type(nodo).__name__}'
		method = getattr(self, method_name, self.no_visitar)
		return method(nodo, contexto)

	def no_visitar(self, nodo, contexto):
		raise Exception(f'No visitar_{type(nodo).__name__} ')

	##########visitando nodos########################

	def visitar_NodoNumero(self, nodo, contexto):
		return ResultadoEJ().exito(
			Numero(nodo.tok.valor).poner_contexto(contexto).poner_pos(nodo.pos_inicio, nodo.pos_fin)
		)

	def visitar_NodoCadena(self, nodo, contexto):
		return ResultadoEJ().exito(
			Cadena(nodo.tok.valor).poner_contexto(contexto).poner_pos(nodo.pos_inicio, nodo.pos_fin)
		)
	
	def visitar_NodoADVar(self,nodo,contexto):
		res= ResultadoEJ()
		nombre_var=nodo.nombre_var_tok.valor
		valor=contexto.tabla_sim.get(nombre_var)

		if not valor:
			return res.fallo(ErrorEJ(nodo.pos_inicio,nodo.pos_fin,f'{nombre_var} no esta definida',contexto))
		
		valor=valor.copiar().poner_pos((nodo.pos_inicio,nodo.pos_fin)).poner_contexto(contexto)
		return res.exito(valor)

	def visitar_NodoDVar(self,nodo,contexto):
		res= ResultadoEJ()
		nombre_var=nodo.nombre_var_tok.valor
		valor=res.registro(self.visitar(nodo.valor_nodo,contexto))
		if res.error : return res

		contexto.tabla_sim.set(nombre_var,valor)
		return res.exito(valor)

	def visitar_NodoOP(self, nodo, contexto):
		res = ResultadoEJ()
		left = res.registro(self.visitar(nodo.nodo_iz, contexto))
		if res.error: return res
		right = res.registro(self.visitar(nodo.nodo_der, contexto))
		if res.error: return res

		if nodo.token_op.tipo == TT_MAS:
			result, error = left.sumar_a(right)
		elif nodo.token_op.tipo == TT_MENOS:
			result, error = left.restar_a(right)
		elif nodo.token_op.tipo == TT_MUL:
			result, error = left.mutiplicar_a(right)
		elif nodo.token_op.tipo == TT_DIV:
			result, error = left.dividir_a(right)
		elif nodo.token_op.tipo == TT_POT:
			result, error = left.potenciar_por(right)
		elif nodo.token_op.tipo == TT_E:
			result, error = left.obt_comp_equi(right)
		elif nodo.token_op.tipo == TT_NE:
			result, error = left.obt_comp_no_equi(right)
		elif nodo.token_op.tipo == TT_MEN:
			result, error = left.obt_comp_menor(right)
		elif nodo.token_op.tipo == TT_MAY:
			result, error = left.obt_comp_mayor(right)
		elif nodo.token_op.tipo == TT_MENE:
			result, error = left.obt_comp_menor_equi(right)
		elif nodo.token_op.tipo == TT_MAYE:
			result, error = left.obt_comp_mayor_equi(right)
		elif nodo.token_op.partido(TT_PALABRACLAVE,'and'):
			result, error = left.operacion_and(right)
		elif nodo.token_op.partido(TT_PALABRACLAVE, 'or'):
			result, error = left.operacion_or(right)

		if error:
			return res.fallo(error)
		else:
			return res.exito(result.poner_pos(nodo.pos_inicio, nodo.pos_fin))

	def visitar_NodoP(self, nodo, contexto):
		res = ResultadoEJ()
		number = res.registro(self.visitar(nodo.nodo, contexto))
		if res.error: return res

		error = None

		if nodo.token_op.tipo == TT_MENOS:
			number, error = number.mutiplicar_a(Numero(-1))
		elif nodo.token_op.partido(TT_PALABRACLAVE,'NOT'):
			number,error= number.noad()

		if error:
			return res.fallo(error)
		else:
			return res.exito(number.poner_pos(nodo.pos_inicio, nodo.pos_fin))

	def visitar_Nodoif(self,nodo,contexto):
		res= ResultadoEJ()
		for codicion, expr in nodo.casos:
			valor_condicion= res.registro(self.visitar(codicion,contexto))
			if res.error: return res

			if valor_condicion.is_true():
				valor_expr=res.registro(self.visitar(expr,contexto))
				if res.error: return res
				return res.exito(valor_expr)
		
		if nodo.caso_else:
			valor_else=res.registro(self.visitar(nodo.caso_else,contexto))
			if res.error: return res
			return res.exito(valor_else)
		
		return res.exito(None)

	def visitar_Nodofor(self,nodo,contexto):
		res=ResultadoEJ()
		elementos=[]
		valor_inicial=res.registro(self.visitar(nodo.valor_var_nodo,contexto))
		if res.error: return res
		
		valor_final=res.registro(self.visitar(nodo.valor_fin_nodo,contexto))
		if res.error: return res

		if nodo.valor_paso_nodo:
			valor_paso=res.registro(self.visitar(nodo.valor_paso_nodo,contexto))
			if res.error: return res
		else:
			valor_paso=Numero(1)
		
		i=valor_inicial.valor
		if valor_paso.valor>=0:
			condicion=lambda: i < valor_final.valor
		else:
			condicion=lambda: i > valor_final.valor
		
		while condicion():
			contexto.tabla_sim.set(nodo.nom_var.valor,Numero(i))
			i += valor_paso.valor
			elementos.append(res.registro(self.visitar(nodo.cuerpo,contexto)))
			if res.error: return res
		
		return res.exito(Lista(elementos).poner_contexto(contexto).poner_pos(nodo.pos_inicio,nodo.pos_fin))

	def visitar_Nodowhile(self,nodo,contexto):
		res = ResultadoEJ()
		elementos=[]
		while True:
			condicion=res.registro(self.visitar(nodo.condicion_nodo,contexto))
			if res.error:  return res

			if not condicion.is_true(): break
			elementos.append(res.registro(self.visitar(nodo.cuerpo,contexto)))
			if res.error: return res
		return res.exito(Lista(elementos).poner_contexto(contexto).poner_pos(nodo.pos_inicio,nodo.pos_fin))
	
	def visitar_NodoLista(self,nodo,contexto):
		res=ResultadoEJ()
		ele=[]
		for nodos_elementos in nodo.nodos_elementos:
			ele.append(res.registro(self.visitar(nodos_elementos,contexto)))
			if res.error: return res
		
		return res.exito(Lista(ele).poner_contexto(contexto).poner_pos(nodo.pos_inicio,nodo.pos_fin))

	def visitar_Nodofun(self,nodo,contexto):
		res = ResultadoEJ()
		nombre_fun= nodo.nom_fun.valor if nodo.nom_fun else None
		cuerpo=nodo.cuerpo
		argumentos=[nom_args.valor for nom_args in nodo.nom_args]
		valor_fun=Funcion(nombre_fun,cuerpo,argumentos).poner_contexto(contexto).poner_pos(nodo.pos_inicio,nodo.pos_fin)

		if nodo.nom_fun:
			contexto.tabla_sim.set(nombre_fun,valor_fun)
		return res.exito(valor_fun)
	
	def visitar_Nodollamada(self,nodo,contexto):
		res=ResultadoEJ()
		argumentos=[]

		valor_llamar= res.registro(self.visitar(nodo.nodo_fun_llamar,contexto))
		if res.error: return res
		valor_llamar.copiar().poner_pos(nodo.pos_inicio, nodo.pos_fin)

		for nodos_args in nodo.nodos_args:
			argumentos.append(res.registro(self.visitar(nodos_args,contexto)))
			if res.error: return res
		
		valor_retornar=res.registro(valor_llamar.ejecutar(argumentos))
		if res.error: return res
		valor_retornar=valor_retornar.copiar().poner_pos(nodo.pos_inicio,nodo.pos_fin).poner_contexto(contexto)
		return res.exito(valor_retornar)
#######################################
# RUN
global_tabla_sim=Tablasim()
global_tabla_sim.set('NULL',Numero.null)
global_tabla_sim.set('TRUE',Numero.falso)
global_tabla_sim.set('FALSE',Numero.verdadero)
global_tabla_sim.set('math_pi',Numero.pi)
global_tabla_sim.set('print',Funcion_inter.print)
global_tabla_sim.set('print_ret',Funcion_inter.print_ret)
global_tabla_sim.set('input',Funcion_inter.input)
global_tabla_sim.set('input_int',Funcion_inter.input_int)
global_tabla_sim.set('lim',Funcion_inter.limpiar)
global_tabla_sim.set('es_numero',Funcion_inter.es_numero)
global_tabla_sim.set('es_cadena',Funcion_inter.es_cadena)
global_tabla_sim.set('es_lista',Funcion_inter.es_lista)
global_tabla_sim.set('es_funcion',Funcion_inter.es_funcion)
global_tabla_sim.set('agregar',Funcion_inter.agregar)
global_tabla_sim.set('pop',Funcion_inter.pop)
global_tabla_sim.set('conca',Funcion_inter.conca)
global_tabla_sim.set('sqrt',Funcion_inter.sqrt)
global_tabla_sim.set('aleatorio_ent',Funcion_inter.aleatorio_ent)
def run(nom_archivo, texto):
	# Generar tokens
	lexer = Lexer(nom_archivo, texto)
	tokens, error = lexer.tokenizar()
	#print(tokens)
	if error: return None, error
	# generar arbol de sintaxis
	parser = Parser(tokens)
	ast = parser.parse()
	if ast.error: return None, ast.error
	#print(ast.nodo)
	# Run 
	interpreter = Interpreter()
	context = Contexto('<programa>')
	context.tabla_sim=global_tabla_sim
	result = interpreter.visitar(ast.nodo, context)
	return result.valor, result.error