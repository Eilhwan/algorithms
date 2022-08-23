package StructuralPatterns._06_adapter.security;

public interface UserDetailService {

    UserDetails loadUser(String username);
}
