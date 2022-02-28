/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
/**
 *
 * @author horacio
 */
public class escribir {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
         try{
            Class.forName("com.mysql.cj.jdbc.Driver");
            try (Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/test?useTimezone=true&serverTimezone=UTC","root","Pepito28")) {
                String Inser = "INSERT INTO test1 VALUES("+"'peres'"+","+"212213"+","+"39);";
                Statement stmt= con.createStatement();
                stmt.executeUpdate(Inser);
                con.close();
                //root@localhost:3306
                //jdbc:mysql://localhost:3306/?user=root
            }
        }
        catch(ClassNotFoundException | SQLException e){
            System.out.println(e);
        }
    }
    
}
