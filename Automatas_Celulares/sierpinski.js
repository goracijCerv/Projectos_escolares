//Implementacion de el triangulo de sierpinski
let ancho = 600;
let alto = 600;
let nivel = 10;

function setup() {
    createCanvas(alto, ancho);

}
//funcion de color random
function getcolorRand() {

    return color(
        random(0, 255),
        random(0, 255),
        random(0, 255),
    );
}
//dibujar triangulos
function Dtrian(p1, p2, p3) {
    fill(getcolorRand());

    triangle(p1.x, p1.y, p2.x, p2.y, p3.x, p3.y)
}

function Puntomedio(p1, p2) {
    return createVector((p1.x + p2.x) / 2, (p1.y + p2.y) / 2);
}

function sierp(trian, ni) {
    if (ni == nivel) {
        return;
    }
    let m = Puntomedio(trian.p1, trian.p2);
    let m2 = Puntomedio(trian.p2, trian.p3);
    let m3 = Puntomedio(trian.p3, trian.p1);
    //dibujamos el primer triangulo de nivel corespondiente
    let t0 = new Trian(m, m2, m3);
    t0.dibujar();
    //establecemos los sub triangulos del nivel corespondeinte
    let t1 = new Trian(trian.p1, m, m3);
    let t2 = new Trian(trian.p2, m, m2);
    let t3 = new Trian(trian.p3, m2, m3);
    sierp(t1, ni + 1);
    sierp(t2, ni + 1);
    sierp(t3, ni + 1);
}

function draw() {
    background(0);
    //dibujando las lineas
    let p1 = createVector(ancho / 2, 0);
    let p2 = createVector(0, alto);
    let p3 = createVector(ancho, alto);
    //creamos nuestro triangulo
    let t = new Trian(p1, p2, p3);
    t.dibujar();
    sierp(t, 0);
}

//clase de triangulo establece la base para que se generen los triangulos mas pequeños
class Trian {
    constructor(p1, p2, p3) {
        this.p1 = p1;
        this.p2 = p2;
        this.p3 = p3;
    }
    dibujar() {
        Dtrian(this.p1, this.p2, this.p3);
    }
}