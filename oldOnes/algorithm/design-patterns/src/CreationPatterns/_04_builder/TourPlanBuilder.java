package CreationPatterns._04_builder;

import java.time.LocalDate;

public interface TourPlanBuilder {

    TourPlanBuilder newInstance();

    TourPlanBuilder title(String title);

    TourPlanBuilder nightAndDays(int nights, int days);

    TourPlanBuilder startDate(LocalDate localDate);

    TourPlanBuilder whereToStay(String whereToStay);

    TourPlanBuilder addPlan(int day, String plan);

    TourPlan getPlan();


}
