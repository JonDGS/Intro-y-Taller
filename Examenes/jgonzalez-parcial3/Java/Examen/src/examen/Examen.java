package examen;

import java.util.Scanner;
        
public class Examen {

    public Examen(){
        
    }
    public static void main(String[] args) {
        Examen test = new Examen();
        test.contar();
        test.ordenar(int[] {1,2,3,4,5,6,7});
        
    }
    public void contar(){
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un numero: ");
        int numero = entrada.nextInt();
        int numero_o = numero;
        int indice = 0;
        if(numero == 0){
            System.out.println(numero_o + " tiene 0 digitos");
        }
        while((numero /10) != numero){
            numero = numero / 10;
            indice += 1;
        }
        System.out.println(numero_o + " tiene " + indice + " digitos");
    }
    public int encontrar(int[] lista){
        int indice = 0;
        int min = 0;
        for (int i=0; i<(lista.length); i++){
            if(min > lista[i + 1]){
                indice = i + 1;
            }
            else{
                if(min < lista[i + 1]);
                    indice = indice;
                }
            else{
                 if(min = lista[i+1]);
            }
        }
        return indice;    
    }
    public void ordenar(int[] lista){
        int[] nueva = lista;
        int longitud = lista.length;
        for (int i=0; i<longitud; i++){
            int indice = encontrar(lista);
            nueva += [lista[indice]];
            lista = lista[indice-1:] + lista[:indice];
            System.out.println(nueva);
        }
    }
    
    
}
