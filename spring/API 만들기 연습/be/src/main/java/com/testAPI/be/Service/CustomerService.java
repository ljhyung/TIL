package com.testAPI.be.Service;

import com.testAPI.be.Entity.Customer;
import com.testAPI.be.Repository.CustomerRepository;
import com.testAPI.be.ResDto.CustomerResDto;
import lombok.AllArgsConstructor;
import org.springframework.stereotype.Service;


import java.util.List;
import java.util.stream.Collectors;

@Service
@AllArgsConstructor
public class CustomerService {
    private final CustomerRepository customerRepository;


    public List<CustomerResDto> getCustomer(String keyword) {
        List<Customer> customerList1 = customerRepository.findCustomersByCodeContaining(keyword);
        List<Customer> customerList2 = customerRepository.findCustomersByNameContaining(keyword);
        List<Customer> customerList3 = customerRepository.findCustomersByHpContaining(keyword);
        customerList1.addAll(customerList2);
        customerList1.addAll(customerList3);

        try {
            Integer keywordNum = Integer.parseInt(keyword);
            List<Customer> customerList4 = customerRepository.findCustomersBySerialEquals(keywordNum);
            customerList1.addAll(customerList4);
            List<Customer> newCustomerList = customerList1.stream().distinct().collect(Collectors.toList());
            return CustomerResDto.fromList(newCustomerList);
        } catch (NumberFormatException e) {
            List<Customer> newCustomerList = customerList1.stream().distinct().collect(Collectors.toList());
            return CustomerResDto.fromList(newCustomerList);
        }

    }
}
