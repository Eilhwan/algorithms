package CreationPatterns._05_prototype;

public class App {
    public static void main(String[] args) throws CloneNotSupportedException {
        GithubRepository repository = new GithubRepository();
        GithubIssue issue = new GithubIssue(repository);


        repository.setName("pythonTutorial");
        repository.setUser("Eilhwan");

        issue.setId(1);
        issue.setTitle("How to set-up Python3");

        String url = issue.getUrl();
        System.out.println(url);

        GithubIssue clone = (GithubIssue) issue.clone();

        System.out.println(clone.getUrl());
        System.out.println(clone != issue);
        System.out.println(clone.equals(issue));
        System.out.println(clone.getClass() == issue.getClass());

        System.out.println(clone.getRepository() == issue.getRepository());
        // TODO clone != githubIssue
        // TODO clone.equals(githubIssue) => true




    }
}
