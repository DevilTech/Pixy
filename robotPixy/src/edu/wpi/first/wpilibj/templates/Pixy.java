

package edu.wpi.first.wpilibj.templates;

import edu.wpi.first.wpilibj.SPIDevice;


public class Pixy {
    SPIDevice pixy;
    public Pixy (int startingPosition){
        pixy = new SPIDevice(1, startingPosition + 3, startingPosition + 2, startingPosition + 1, startingPosition);
    }
    
    public byte[] read(){
        long l = pixy.transfer(0,16);
        
        if (l == 0xaa55 || l == 0x55aa){
            byte[] b = new byte[4];
            l = pixy.transfer(0,32);
            for (int i = 0; i < b.length; i++) {
                b[i] = (byte) (l & 0xff);
                l >>= 8;
            }
             return b;       
        }
        else{
            /*
            byte[] b = new byte[4];
            for (int i = 0; i < b.length; ++i) {
                b[i] = (byte) (l >> (16-(i * 2)));
            }
            return b;
                    */
            return new byte[]{0};
                    
        }
        
    }
}
