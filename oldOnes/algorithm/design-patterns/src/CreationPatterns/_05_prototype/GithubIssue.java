package CreationPatterns._05_prototype;

import java.util.Objects;

public class GithubIssue implements Cloneable {
    private int id;

    private String title;

    private GithubRepository repository;

    public GithubIssue(GithubRepository repository) {
        this.repository = repository;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public GithubRepository getRepository() {
        return repository;
    }

    public void setRepository(GithubRepository repository) {
        this.repository = repository;
    }

    public String getUrl() {
        return "https://github.com/" + this.getRepository().getUser() + "/" + this.getRepository().getName() + "/" + this.getId();
    }

    @Override
    protected Object clone() throws CloneNotSupportedException {
        GithubRepository repository = new GithubRepository();
        repository.setUser(this.getRepository().getUser());
        repository.setUser(this.getRepository().getName());
        GithubIssue issue = new GithubIssue(repository);

        issue.setId(this.getId());
        issue.setTitle(this.getTitle());

        return issue;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        GithubIssue issue = (GithubIssue) o;
        return id == issue.id && Objects.equals(title, issue.title) && Objects.equals(repository, issue.repository);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id, title, repository);
    }
}
