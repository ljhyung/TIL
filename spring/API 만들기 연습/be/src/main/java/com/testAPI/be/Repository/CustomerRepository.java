package com.testAPI.be.Repository;

import com.testAPI.be.Entity.Customer;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface CustomerRepository extends JpaRepository<Customer, Long> {
    List<Customer> findCustomersByNameContaining(String keyword);
    List<Customer> findCustomersByCodeContaining(String keyword);
    List<Customer> findCustomersByHpContaining(String keyword);

    List<Customer> findCustomersBySerialEquals(Integer keywordNum);

}
