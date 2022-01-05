package StructuralPatterns._06_adapter;

import StructuralPatterns._06_adapter.security.UserDetailService;
import StructuralPatterns._06_adapter.security.UserDetails;

public class AccountUserDetailsService implements UserDetailService {

    private AccountService accountService;

    public AccountUserDetailsService (AccountService accountService) {
        this.accountService = accountService;
    }

    @Override
    public UserDetails loadUser(String username) {
        Account account = accountService.findAccountByUsername(username);
        return new AccountUserDetails(account);
    }
}
