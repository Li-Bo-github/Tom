/**
 * class InputOutput
 *
 * Contains input/output methods provided by the IBO for primitive data types and Strings
 *
 * @authors Kostas Dimitriou & Markos Hatzitaskos
 * @version 1.0
 */
public abstract class InputOutput
{
    static void output(String information){
        System.out.println(information);
    }

    static void output(int information){
    System.out.println(information);
}

    static void output(char information){
        System.out.println(information);
    }


    static String input(String Prompt)
    {String inputLine = " ";
    System.out.print(Prompt);
    try
    {inputLine = (new java.io.BufferedReader(new java.io.InputStreamReader(System.in))).readLine();}
    catch (Exception e)
    {String err = e.toString();
        System.out.println(err);
        inputLine = " ";
    }
    return inputLine;
    }

    static int inputInt()
    {return inputInt(" ");}

    static String inputString(String prompt)
        {return input(prompt);}

    static char inputChar(String prompt)
    {char result=(char)0;
    try{result=input(prompt).charAt(0);}
    catch (Exception e){result = (char)0;}
    return result;}

    static int inputInt(String prompt)
    {int result = 0;
        try {result = Integer.valueOf(input(prompt).trim()).intValue();}
        catch (Exception e) {result = 0;}
        return result;
}
}
