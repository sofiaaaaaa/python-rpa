
class EnumTest {


	//Enum 상수값 가져오기 
	//source: https://stackoverflow.com/questions/35140408/how-to-get-value-from-a-java-enum/35140425
	public static void main(String[] args) {
		System.out.println(Mode.Run.getValue());
	}

	public enum Mode {
		Run("R"), Dev("D");

		private String value;

		Mode(String value) {
			this.value = value;
		}

		public String getValue() {
			return value;
		}
	}
}