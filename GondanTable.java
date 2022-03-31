/*
@author <a href="mailto:liujq417119@outlook.com">Qbebee</a>
*/

import java.awt.*;
import java.awt.print.*;
import javax.swing.*;
import java.io.*;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;
import java.util.ArrayList;
import java.util.Properties;
import javax.swing.table.*;
import java.sql.*;
import javax.sql.rowset.*;

public class GondanTable{
    public static void main(String[] args) {
        EventQueue.invokeLater(() ->  {
            PlanetTableFrame frame = new PlanetTableFrame();
            frame.setTitle("=====\u5de5\u5355\u6570\u636e\u8868=====");
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setVisible(true);
        });
    }
}

class PlanetTableFrame extends JFrame {
    public String[] columnNames = {"\u6d41\u6c34\u53f7","\u7ffb\u5806\u65e5\u671f","\u59d3\u540d","\u677f\u6570","\u6563\u4ef6\u6570","\u603b\u4ef6\u6570"};
    public String[] clerks = {"\u5218\u5065\u5168","\u5218\u56fd\u4eae","\u5218\u632f\u826f","\u76db\u6587\u660e","\u77bf\u660e","\u9ec4\u4f1f\u6797","\u5468\u632f\u5174"};

    public PlanetTableFrame(){
        try{
			JTable table = new JTable(lookupGD(),columnNames);
			table.setAutoCreateRowSorter(true);
			table.setFillsViewportHeight(true);
			
			//TableRowSorter sorter = new TableRowSorter<TableModel>(model);
   
			TableColumnModel columnModel = table.getColumnModel();
			//TableColumn tatColumn = columnModel.getColumn(6);
			//table.removeColumn(tatColumn);
			add(new JScrollPane(table),BorderLayout.CENTER);
			JButton printButton = new JButton("\u6253\u5370PDF");
			printButton.addActionListener(event ->{
				try{table.print();}catch(SecurityException  | PrinterException ex){ ex.printStackTrace();}});
      
			JPanel buttonPanel = new JPanel();
			buttonPanel.add(printButton);
			add(buttonPanel,BorderLayout.SOUTH);
			pack();
			
        
        }catch(SQLException|IOException e){
			e.printStackTrace();
        }
    }
    
    class MyTableModel extends AbstractTableModel{
    
		private int id;
		private String fadriq;
		private String name;
		private int bans;
		private int sanj;
		private int ybans;
		
		private String ysanj;
		private int totals;
		private int rows;
		private int columns;
    
		public MyTableModel(int id,String fq,String nm,int bs,int sj,int yb,String ys,int zj){
			this.id=id;
			this.fadriq=fq;
			this.name=nm;
			this.bans=bs;
			this.sanj=sj;
			this.ybans=yb;
			this.ysanj=ys;
			this.totals=zj;
		}
		public MyTableModel(int rs,int cs){
			rows=rs;
			columns=cs;
		}
		public MyTableModel(){}
		public int getRowCount(){
			return rows;
		}
		
		public int getColumnCount(){
			return columns;
		}
		
		public Object getValueAt(int row,int column){
			return 0.0;
		}
		
		public String getColumnName(int column){
			return columnNames[column];
		}
		
		public boolean isCellEditable(int row,int column){
			return true;
		}
		
		public void setValueAt(int row,int column){
			//Object value = model.getValueAt(row,column);
		}
    }
    
    public static Connection getConnection()throws SQLException,IOException{
		Properties props = new Properties();
		try
			(InputStream in = Files.newInputStream(Paths.get("database.properties")))
		{		
			{props.load(in);}
			String drivers = props.getProperty("jdbc.drivers");
			if(drivers!=null){ System.setProperty("jdbc.drivers",drivers);}
			String url = props.getProperty("jdbc.url");
			String username = props.getProperty("jdbc.username");	
			String password = props.getProperty("jdbc.password");
			
			return DriverManager.getConnection(url,username,password);
		}
    }
    
    public static void getData(ResultSet rs) throws SQLException,IOException{
		
		try{
			String eachrow =null;
    
			File f = new File("d:\\ryproject\\mydata.txt");
			f.createNewFile();
			FileWriter fw = new FileWriter(f,true);
			BufferedWriter out = new BufferedWriter(fw);
			while(rs.next()){
			
				eachrow ="{"+rs.getInt(1)+",\""+rs.getString(2)+"\""+",\""+rs.getString(3)+"\""+","+rs.getInt(4)+","+rs.getInt(5)+","+rs.getInt(6)+"},\n";
				out.write(eachrow);
				out.flush();	
			}
			
			out.close();
		}catch(SQLException|IOException e){e.printStackTrace();}

    }
    
    public static Object[][] lookupGD()throws SQLException,IOException {
		ResultSet rs = null;
		Connection conn = null;
		Statement stat = null;
		ResultSetMetaData meta = null;
		Object[][] data =null;
		ArrayList<Object> al = new ArrayList<Object>();
		int rws =0;
		int cols =0;
		String sql ="select id,fadriq,name,bans,sanj,totals from gondan_202203m  order by name,fadriq  ";
		System.out.println(sql);
		try{	 conn = getConnection();
				 stat = conn.createStatement(ResultSet.TYPE_FORWARD_ONLY,ResultSet.CONCUR_READ_ONLY);
				{
					rs = stat.executeQuery(sql);
					meta = rs.getMetaData();
					cols = meta.getColumnCount();
					
					while(rs.next()){
						for(int i=0;i<cols;i++){
							al.add(rs.getObject(i+1)) ;
						
						}
						rws++;
					}
					

					System.out.println("hello world"+al.size());	
				}
				int n=0;
				for(int m=0; m<al.size(); m++){
					System.out.print(al.get(m)+" ");
					if((m+1)%cols==0){
						n++;
						System.out.println("\n");
					}
					
				}
				data = new Object[rws][cols];
				System.out.println("size="+data.length+" rows="+rws);
				int z=al.size();
				for(int x=0;x<rws;x++){
					for(int y=0;y<cols;y++){
					
						data[x][y] =al.get(al.size()-z);	
						z--;
					}
					
				}
				System.out.println("data="+data+"	z="+z);
		}catch(SQLException|IOException ex){ex.printStackTrace();}
		
		return data;
    }
}


