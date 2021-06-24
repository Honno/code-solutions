import java.util.Scanner;
import java.util.InputMismatchException;
import java.util.EnumSet;

public class OSTypeEnumReverse
{
    enum OS { ANDROID, IOS, MACOSX, WINDOWS8, WP8, VXWORKS }
    
    enum OSType { DESKTOP, EMBEDDED, MOBILE }
    
    private static <E extends Enum<E>> E getEnumElement(String elementTypeName, Class<E> elementType)
    {
        boolean haveResult = false;
        E result = null;
        Scanner stdin = new Scanner(System.in);
        
        while ( ! haveResult )
        {
            System.out.print("Input " + elementTypeName + ": ");
            try
            {
                result = Enum.valueOf(elementType, stdin.next().toUpperCase());
                haveResult = true;
            }
            catch (IllegalArgumentException e)
            {
                System.out.println("Not a valid " + elementTypeName + ".");
                stdin.nextLine(); // skip the invalid input
            }
        }
        
        return result;
    }
  
    private static OS ostype2OS(OSType ostype)
    {
        OS os = null;
        
        switch (ostype)
        {
        case DESKTOP:
            os = OS.MACOSX;
            break;
        case EMBEDDED:
            os = OS.VXWORKS;
            break;
        case MOBILE:
            os = OS.ANDROID;
            break;
        }
        
        return os;
    }

    public static void main(String[] args)
    {
        System.out.print("Known Types = ");
        for (OSType t : EnumSet.allOf(OSType.class)) 
        {
            System.out.print(t + " ");
        }
        System.out.println();
        
        OSType ostype = getEnumElement("operating system type", OSType.class);
        System.out.println(ostype + " is of type: " + ostype2OS(ostype));
    }
}
