class Solution {
    public String complexNumberMultiply(String num1, String num2) {
        String[] operand1 = num1.split("\\+");
        String[] operand2 = num2.split("\\+");
        
        int op1 = Integer.parseInt(operand1[0]);
        int op2 = Integer.parseInt(operand1[1].split("i")[0]);
        int op3 = Integer.parseInt(operand2[0]);
        int op4 = Integer.parseInt(operand2[1].split("i")[0]);
        
        String first = Integer.toString(op1 * op3 + op2 * op4 * -1);
        String second = Integer.toString(op1 * op4 + op2 * op3) + "i";
        
        return first + "+" + second;
    }
}