import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;

public class CollectionSortTest {
	
    // Java에서 HashMap 유형의 배열의 특정키를 오름차순, 내림차순으로 정렬하는 방법 
	private static HashMap<String, Object> getDayMap(String day) {

		HashMap<String, Object> map = new HashMap<>();
		map.put("Day", "2021-11-0"+ day);
		return map;
	}

	public static void main(String[] args) {
			
			List<HashMap<String, Object>> list = new ArrayList<HashMap<String, Object>>();
			list.add(getDayMap("1"));
			list.add(getDayMap("5"));
			list.add(getDayMap("7"));
			list.add(getDayMap("2"));
			list.add(getDayMap("6"));
			list.add(getDayMap("9"));
			list.add(getDayMap("4"));
			for(int i=0; i<list.size(); i++) System.out.println(list.get(i));
			
			// Day(String) 오름차순
			Collections.sort(list, new Comparator<HashMap<String, Object>>() {
				@Override
				public int compare(HashMap<String, Object> o1, HashMap<String, Object> o2) {
					String day1 = (String) o1.get("Day");
					String day2 = (String) o2.get("Day");
					return day1.compareTo(day2);
				}
			});
			System.out.println();
			for(int i=0; i<list.size(); i++) System.out.println(list.get(i));
			
			// Day(String) 내림차순
			Collections.sort(list, new Comparator<HashMap<String, Object>>() {
				@Override
				public int compare(HashMap<String, Object> o1, HashMap<String, Object> o2) {
					String day1 = (String) o1.get("Day");
					String day2 = (String) o2.get("Day");
					return day2.compareTo(day1);
				}
			});
			System.out.println();
			for(int i=0; i<list.size(); i++) System.out.println(list.get(i));
			
		
	}

}
