class Solution {
    public boolean isValid(String s) {
        Stack<String> stack = new Stack<String>();

        HashMap<String, String> hashmap = new HashMap<>(Map.of(
                ")", "(",
                "}", "{",
                "]", "["));

        for (int p = 0; p < s.length(); p++) {
            String currentChar = Character.toString(s.charAt(p));

            if (hashmap.containsValue(currentChar)) {
                stack.push(currentChar);
            } else if (!stack.isEmpty() && hashmap.get(currentChar).equals(stack.peek())) {
                stack.pop();
            } else {
                return false;
            }
        }

        return stack.isEmpty();
    }

}
