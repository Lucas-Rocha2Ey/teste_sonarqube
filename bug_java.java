public class HelloWorld {
    public static void main(String[] args) {
Logger.getLogger(HelloWorld.class.getName()).log(Level.INFO, "Hello, World!");

        // Declaração de uma variável não utilizada - SonarQube deve detectar isso como um code smell.

    }
}
