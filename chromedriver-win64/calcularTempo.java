import java.time.LocalTime;
import java.time.Duration;

public class calcularTempo {
    public static void main(String[] args) {
        
        LocalTime horario1 = LocalTime.of(10, 3, 0); // Horário inicial
        LocalTime horario2 = LocalTime.of(10, 45, 30); // Horário final

        Duration diferenca = Duration.between(horario1, horario2);
        long diferencaSegundos = diferenca.getSeconds();

        System.out.println("Horário 1: " + horario1);
        System.out.println("Horário 2: " + horario2);
        System.out.println("Diferença em segundos: " + diferencaSegundos);
    }
}