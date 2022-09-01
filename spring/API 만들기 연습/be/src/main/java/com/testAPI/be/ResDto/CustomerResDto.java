package com.testAPI.be.ResDto;

import com.testAPI.be.Entity.Customer;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;

import java.util.ArrayList;
import java.util.List;
@Builder
@Data
@AllArgsConstructor
public class CustomerResDto {
    private String name;
    private Integer serial;
    private String code;
    private String hp;

    public static ArrayList<CustomerResDto> fromList(List<Customer> customerList) {
        ArrayList<CustomerResDto> listCustomerDto = new ArrayList<>();
        int i = 0;
        while (i < customerList.size()) {
            CustomerResDto customerResDto = CustomerResDto.builder()
                    .name(customerList.get(i).getName())
                    .serial(customerList.get(i).getSerial())
                    .code(customerList.get(i).getCode())
                    .hp(customerList.get(i).getHp())
                    .build();
            listCustomerDto.add(customerResDto);
            i++;
        }
        return listCustomerDto;
    }

}
