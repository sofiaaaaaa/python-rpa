package com.example.unitTest;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class TestController {
  @GetMapping("/ping") 
  public String ping() {
    return "ping";
  }
  
  @GetMapping("/exception") 
  public void error() {
    throw new RuntimeException("call exception!!");
  }
  
  public static void main(String[] args) {
    // TODO Auto-generated method stub
    
  }
  
}
