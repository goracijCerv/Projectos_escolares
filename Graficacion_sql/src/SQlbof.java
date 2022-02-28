/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;
/**
 *
 * @author horacio
 */
public class SQlbof  {
    String nom;
    int id;
    public void SQLbof(){
        this.nom=null;
        this.id=0;
    }
    public void incertar(String nomh, int inden){
        this.nom=nomh;
        this.id=inden;
        try{
            Class.forName("com.mysql.cj.jdbc.Driver");
            try (Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/proyecto?useTimezone=true&serverTimezone=UTC","root","Pepito28")) {
                String Inser = "INSERT INTO altas(ID,Nombre) VALUES("+this.id+","+"'"+this.nom+"');";
                Statement stmt= con.createStatement();
                stmt.executeUpdate(Inser);
                
                con.close();
            }
        }
        catch(ClassNotFoundException | SQLException e){
            System.out.println(e);
        }
    }
    public void editar1(int reg, String aa){
        String assde=aa;
        int assder=reg;
        try{
            Class.forName("com.mysql.cj.jdbc.Driver");
            try (Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/proyecto?useTimezone=true&serverTimezone=UTC","root","Pepito28")) {
                String Inser = "UPDATE altas SET Nombre='"+assde+"'"+" WHERE ID ="+assder+";";
                Statement stmt= con.createStatement();
                stmt.executeUpdate(Inser);
                
                con.close();
            }
        }
        catch(ClassNotFoundException | SQLException e){
            System.out.println(e);
        }
    }
    public void editar2(int reg34, String awa){
         String assde=awa;
        int assder=reg34;
        try{
            Class.forName("com.mysql.cj.jdbc.Driver");
            try (Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/proyecto?useTimezone=true&serverTimezone=UTC","root","Pepito28")) {
                String Inser = "UPDATE altas SET ID="+assder+" WHERE Nombre ='"+assde+"';";
                Statement stmt= con.createStatement();
                stmt.executeUpdate(Inser);
                
                con.close();
            }
        }
        catch(ClassNotFoundException | SQLException e){
            System.out.println(e);
        }
    }
    public void Borrar(int assdar){
        int asa= assdar;
        try{
            Class.forName("com.mysql.cj.jdbc.Driver");
            try (Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/proyecto?useTimezone=true&serverTimezone=UTC","root","Pepito28")) {
                String Inser = "DELETE FROM altas WHERE ID ="+asa+";";
                Statement stmt= con.createStatement();
                stmt.executeUpdate(Inser);
                
                con.close();
            }
        }
        catch(ClassNotFoundException | SQLException e){
            System.out.println(e);
        }
    }
}
