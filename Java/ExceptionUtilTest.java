import org.apache.commons.lang3.exception.ExceptionUtils;

class ExceptionUtilTest {
    // ExceptionUtil 메서드 확인하기 
    // https://commons.apache.org/proper/commons-lang/apidocs/org/apache/commons/lang3/exception/ExceptionUtils.html
	public static void main(String[] args) {
		
		try {
		    int a = 1/0;
		} catch(Exception e) {
			System.out.println(String.format("ExceptionUtil.getStackTrace(e) ===> %s", ExceptionUtils.getStackTrace(e)));
			System.out.println(String.format("ExceptionUtil.getRootCause(e) ===> %s", ExceptionUtils.getRootCause(e)));
		}
		//				logger.error(ExceptionUtils.getRootCause(e));


	}

}