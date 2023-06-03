/**
Name        :   Shivani Panchiwala
UTA ID      :   1001982478
Version     :   java 19.0.2 
OS          :   Windows 11
*/

import java.nio.file.Path; 
import java.lang.String;
import java.io.File;

class Total_Size {

    public int get_Total_Size(String path){

        int total_Size = 0;

        if (path == "") {
            path = Path.of("").toAbsolutePath().toString();
        }

        File dir = new File(path);
        File[] dir_contents = dir.listFiles();

        if (dir_contents != null) {
            for (File itemName: dir_contents) {
                if (itemName.isFile()){
                      System.out.println("File = " + itemName + " has size = " + itemName.length() + " Bytes");
                      total_Size += itemName.length();
                }
                else if (itemName.isDirectory()) {
                    System.out.println("Dir = " + itemName);
                    total_Size += get_Total_Size(itemName.toString());
                    System.out.println("------------------------");
                }
            }
        }

        return total_Size;
    }

    public static void main(String[] args) {
        Total_Size total_Size = new Total_Size();
        int total_SizeValue = total_Size.get_Total_Size("");
        System.out.println("*****************************");
        System.out.println("Total Size = " + total_SizeValue + " Bytes");
        System.out.println("*****************************");
    }
}

/**
Code Explanation
----------------
If no path is mentioned then the current directory is explored for its contents.
If the item is a file then its size is stored and if it is directory the same function is called with the directory's path.
This recursion stops when all directories have been explored and file sizes stored.
The final size is returned.
 */