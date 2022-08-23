package CreationPatterns._04_builder;

public class App {
    public static void main(String[] args) {
        TourDirector director = new TourDirector(new DefualtTourPlanBuilder());
        TourPlan plan = director.longBeachPlan();
        System.out.println(plan);
    }
}
