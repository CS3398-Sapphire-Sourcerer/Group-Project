package assignment2; /**
 * assignment2.FileIO reads a file
 * @author Claudia Ortiz
 * @version 1.0
 */

import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Scanner;


public class FileIO {

    /**
     * Reads the file, and parses into a list
     * @param fileName
     * @return stringList
     */
    public ArrayList<String[]> readFile(String fileName) throws Exception {

        Scanner inFile = null;
        ArrayList<String[]> stringList = null;
        try {
            inFile = new Scanner(new FileReader(fileName));
            stringList = new ArrayList<>();


            //read each line and add line to arrayList as a string[]
            while (inFile.hasNext()) {
                String line = inFile.nextLine();
                String[] words = line.split(" ");
                //stringList = {words[0], ... words[n]}
                stringList.add(words);
            }
        }
        catch (IOException e) {
            e.printStackTrace();
            return null;
        } finally {
            if(inFile != null)
                inFile.close();
        }

        return stringList;
    }

    /**
     * Takes an array of string and saves them to a file
     * @param fileName
     * @param strings strings to save to a file
     */
    public void saveFile(String fileName, ArrayList<String> strings) throws Exception {
        PrintWriter out = null;
        try
        {
            out = new PrintWriter(fileName);
            for (String string : strings) {
                out.println(string);
            }
        }
         catch (IOException e) {
              e.printStackTrace();
        } finally {
            if(out != null)
                out.close();
        }
    }
}

