package com.testAPI.be.Controller;

import com.testAPI.be.ResDto.CustomerResDto;
import com.testAPI.be.Service.CustomerService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.media.Content;
import io.swagger.v3.oas.annotations.media.Schema;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.responses.ApiResponses;
import io.swagger.v3.oas.annotations.tags.Tag;
import lombok.AllArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.io.UnsupportedEncodingException;
import java.net.URLDecoder;
import java.util.List;

@RestController
@RequestMapping("/customer")
@AllArgsConstructor
@Tag(name = "customer", description = "사용처 API")
public class CustomerController {
    private final CustomerService customerService;

    @Operation(summary = "get customer", description = "testAPI 사용처 조회하기")
    @ApiResponses({
            @ApiResponse(responseCode = "200", description = "OK", content = @Content(schema = @Schema(implementation = CustomerResDto.class))),
            @ApiResponse(responseCode = "400", description = "BAD REQUEST"),
            @ApiResponse(responseCode = "404", description = "NOT FOUND"),
            @ApiResponse(responseCode = "500", description = "INTERNAL SERVER ERROR")
    })
    @GetMapping("/{keyword}")
    public ResponseEntity<List<CustomerResDto>> getProductDetail(@PathVariable String keyword) throws UnsupportedEncodingException {
        String koreanKeyword = URLDecoder.decode(keyword, "UTF-8");
        return ResponseEntity.ok(customerService.getCustomer(koreanKeyword));
    }

}
