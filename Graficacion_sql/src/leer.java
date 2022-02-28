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
public class leer {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        try{
            Class.forName("com.mysql.cj.jdbc.Driver");
            try (Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/test?useTimezone=true&serverTimezone=UTC","root","Pepito28")) {
                Statement stmt= con.createStatement();
                ResultSet rs=stmt.executeQuery("select *from test1");
                while (rs.next()) {
                    System.out.println(rs.getString(1)+" "+rs.getInt(2)+" "+rs.getInt(3));
                }
                //root@localhost:3306
                //jdbc:mysql://localhost:3306/?user=root
            }
        }
        catch(ClassNotFoundException | SQLException e){
            System.out.println(e);
        }
    }
    
}
