import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<String> week = Arrays.asList("SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT");
        System.out.println(7 - week.indexOf(sc.next()));
    }
}

//提出 #8610824
//問題文
//今日の曜日を表す文字列 S が与えられます。
//S は SUN,MON,TUE,WED,THU,FRI,SAT のいずれかであり、それぞれ日曜日、月曜日、火曜日、水曜日、木曜日、金曜日、土曜日を表します。
//次の日曜日 (あす以降) が何日後か求めてください。
//制約S は SUN,MON,TUE,WED,THU,FRI,SAT のいずれか