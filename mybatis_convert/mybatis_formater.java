import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

class a {
    public static void main(String[] args) throws IOException {
        // FileReader reader = new FileReader("");
        //  int ch; 
        //  while ((ch = reader.read()) != -1) 
        //  { System.out.print((char) ch); }
        // List<String> lines = Files.readAllLines(Paths.get(""));
        // System.out.println(lines);

        String fileName = "C:\\test.log";
        File inputFile = new File(fileName);
        File outputFile = new File(fileName+".new");
        FileInputStream fileInputStream = null;
        BufferedReader bufferedReader = null;
        FileOutputStream fileOutputStream = null;
        BufferedWriter bufferedWriter = null;
        boolean result = false;

        try {
            fileInputStream = new FileInputStream(inputFile);
            fileOutputStream = new FileOutputStream(outputFile);
            bufferedReader = new BufferedReader(new InputStreamReader(fileInputStream));
            bufferedWriter = new BufferedWriter(new OutputStreamWriter(fileOutputStream));

            String line;
            String repLine;
            String originalString = "aaa";
            String replaceString = "qqq";

            while ((line = bufferedReader.readLine()) != null) {
                repLine = line.replaceAll(originalString, replaceString);
                bufferedWriter.write(repLine, 0, repLine.length());
                bufferedWriter.newLine();
                System.out.println(line);
            }

            result = true;
        } catch (IOException ex) {
            ex.printStackTrace();
        } finally {
            // 리소스 해제. 개별적으로 해제한다.
            try {
                bufferedReader.close();
            } catch (IOException ex1) {
                ex1.printStackTrace();
            }

            try {
                bufferedWriter.close();
            } catch (IOException ex2) {
                ex2.printStackTrace();
            }

            if (result) {
                inputFile.delete();
                outputFile.renameTo(new File(fileName));
            }
        }
    }

}

// https://hianna.tistory.com/587 참조 