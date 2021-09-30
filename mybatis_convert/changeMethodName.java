import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Map;

/**
 * 폴더별로 클래스 소스의 클래스명을 파일명과 동일하게 바꿔준다.
 */
class b {
    public static void main(String[] args) throws IOException {
        String servicePath = "C:/";
        String serviceImplPath = "/";
       String[] packageList = {"a"};
       String dummyServiceName = "";
       String packagePath = "";
        
        // 폴더리스트 출력 .
        for (int i = 0; i < packageList.length; i++) {
            File dir = new File(servicePath+packageList[i]);
            File files[] = dir.listFiles();
    
            for (int j = 0; j < files.length; j++) {
                // System.out.println("file: " + files[j]);

                File inputFile = files[j];
                File outputFile = new File(inputFile+"_");
                FileInputStream fileInputStream = null;
                BufferedReader bufferedReader = null;
                FileOutputStream fileOutputStream = null;
                BufferedWriter bufferedWriter = null;
                boolean result = false;

                // System.out.println("name  = "+inputFile.getName());
        
                try {
                    fileInputStream = new FileInputStream(inputFile);
                    fileOutputStream = new FileOutputStream(outputFile);
                    bufferedReader = new BufferedReader(new InputStreamReader(fileInputStream));
                    bufferedWriter = new BufferedWriter(new OutputStreamWriter(fileOutputStream));
        
                    String line;
                    String repLine;
                    while ((line = bufferedReader.readLine()) != null) {
                        // repLine = line.replaceAll("", "");
                        String inputFileClassName = inputFile.getName().replace(".java","");
                        if(line.indexOf(dummyServiceName) > 0) {
                            // 클래스명 변경 
                            if(line.indexOf(inputFileClassName) > -1) {
                                repLine = line;
                            }
                            repLine = line.replace(dummyServiceName, inputFileClassName);
                            bufferedWriter.write(repLine, 0, repLine.length());
                            bufferedWriter.newLine();
                            // System.out.println(repLine + "변경됨");
                            result = true;
                        } else if(line.indexOf(packagePath) > -1) {
                            // 패키지명변경 
                            if(line.indexOf(packageList[i]) > -1) {
                                repLine = line;
                            }
                            repLine = line.replace("", packageList[i]);
                            bufferedWriter.write(repLine, 0, repLine.length());
                            bufferedWriter.newLine();
                            result = true;
                        } else {
                            bufferedWriter.write(line, 0, line.length());
                            bufferedWriter.newLine();
                        }
                    }
        
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
                        System.out.println("changed    : " + inputFile);
                        inputFile.delete();
                        outputFile.renameTo(inputFile);
                    } else {
                        outputFile.delete();
                    }
                }

            }
        }
       

    }

}

// https://hianna.tistory.com/587 참조 