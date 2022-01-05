package StructuralPatterns._06_adapter;

import StructuralPatterns._06_adapter.security.LoginHandler;

public class App {
    public static void main(String[] args) {
        AccountService accountService = new AccountService();
        AccountUserDetailsService accountUserDetailsService = new AccountUserDetailsService(accountService);
        LoginHandler loginHandler = new LoginHandler(accountUserDetailsService);

        String id = loginHandler.login("Eilhwan", "Eilhwan");
        System.out.println(id);
    }
}
