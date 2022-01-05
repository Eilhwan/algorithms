package CreationPatterns._04_builder;

import java.time.LocalDate;

public class TourDirector {

    private DefualtTourPlanBuilder builder;

    public TourDirector(DefualtTourPlanBuilder builder) {
        this.builder = builder;
    }

    public TourPlan cancunPlan(){
        return builder.title("cancun 여행")
                .nightAndDays(3, 4)
                .startDate(LocalDate.of(2021, 7, 21))
                .whereToStay("리조트")
                .addPlan(0, "체크인하고 짐풀기")
                .addPlan(0, "저녁식사")
                .getPlan();
    }

    public TourPlan longBeachPlan(){
        return builder.title("longBeach 여행")
                .nightAndDays(3, 4)
                .startDate(LocalDate.of(2021, 7, 21))
                .whereToStay("리조트")
                .getPlan();
    }

}
