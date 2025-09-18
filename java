import java.util.*;

public class Main {
    public static void main(String[] args) {
        // Массив (список) строк
        List<String> aList = Arrays.asList("a", "b", "c");
        
        // Стек целых чисел
        Stack<Integer> stack = new Stack<>();
        
        // Добавление в стек
        stack.push(1);    // [1]
        stack.push(2);    // [1, 2]
        stack.push(3);    // [1, 2, 3]
        
        // Удаление из стека
        int top = stack.peek();  // получаем верхний элемент
        stack.pop();             // удаляем его из стека
        
        System.out.println("Верхний элемент: " + top);
        System.out.println("Размер стека после pop: " + stack.size());
        System.out.println("Массив: " + aList);
    }
}
