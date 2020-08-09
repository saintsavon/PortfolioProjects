package SchoolProjects;

public class GradeAvg {
    public static void main(String[] args) {   

    // Initializing percents and averages.
        int quizScore1 = 70, quizScore2 = 75, quizScore3 = 80, testScore1 = 90, testScore2 = 85;
        int quizScoreAvg = (quizScore1 + quizScore2 + quizScore3) / 3, testScoreAvg = (testScore1 + testScore2) / 2;

    // Printing quiz and test scores as well as averages for each.
           System.out.println("Quiz Score 1: " + quizScore1 + "%.");
           System.out.println("Quiz Score 2: " + quizScore2 + "%.");
           System.out.println("Quiz Score 3: " + quizScore3 + "%.");
           System.out.println("Test Score 1: " + testScore1 + "%.");
           System.out.println("Test Score 2: " + testScore2 + "%.");
           System.out.println("Quiz Average: " + quizScoreAvg + "%.");
           System.out.println("Test Average: " + testScoreAvg + "%.");

    }
}