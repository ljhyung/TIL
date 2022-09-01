package com.testAPI.be.Entity;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import javax.persistence.*;

@Entity
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
public class Customer {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "name", length = 30, nullable = false)
    private String name;
    @Column(name = "serial", length = 8, nullable = false)
    private Integer serial;
    @Column(name = "hp", length = 11, nullable = true)
    private String hp;
    @Column(name = "code", length = 4, nullable = true)
    private String code;


}
