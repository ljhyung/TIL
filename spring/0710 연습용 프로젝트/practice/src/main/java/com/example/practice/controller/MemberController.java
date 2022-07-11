package com.example.practice.controller;

import com.example.practice.domain.Member;
import com.example.practice.service.MemberService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@Controller
public class MemberController {
    private final MemberService memberService;

    @Autowired
    public MemberController(MemberService memberService) {
        this.memberService = memberService;
    }

    @GetMapping(value = "/members/new")
    public String createForm(){
        return "members/createMemberForm";
    }

    @GetMapping(value = "/members")
    @ResponseBody
    public List list(){
        return memberService.findMembers();
    }

    @GetMapping(value = "/members/{memberId}")
    @ResponseBody
    public Optional<Member> findMember(@PathVariable(value = "memberId") Long id){
        return memberService.findOne(id);
    }

    @DeleteMapping(value = "/members/{memberId}")
    @ResponseBody
    public Long delete(@PathVariable(value = "memberId") Long id){
        return memberService.withdraw(id);
    }

    @PostMapping(value = "/members/new")
    @ResponseBody
    public Long create(MemberForm form){
        Member member = new Member();
        member.setName(form.getName());

        return memberService.join(member);
    }
}






















