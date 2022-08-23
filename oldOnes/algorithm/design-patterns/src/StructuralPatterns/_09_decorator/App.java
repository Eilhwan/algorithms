package StructuralPatterns._09_decorator;

import java.net.http.HttpRequest;

public class App {
    private static boolean enabledSpamFilter = false;

    private static boolean enabledTrimming = true;

    public static void main(String[] args) {
        CommentService commentService = new DefaultCommentService();

        if (enabledSpamFilter) {
            commentService = new SpamFilteringCommentDecorator(commentService);
        }
        if (enabledTrimming) {
            commentService = new TrimmingCommentDecorator(commentService);
        }

        Client client = new Client(commentService);

        client.writeComment("오징어 게임");
        client.writeComment("보는 게 하는 거보다 재미있을 수가 없지...");
        client.writeComment("http://whiteship.me");

//        HttpRequest
    }
}
