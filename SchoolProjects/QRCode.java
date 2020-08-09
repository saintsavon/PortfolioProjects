package SchoolProjects;

import java.util.logging.Level;
import java.util.logging.Logger;
import javafx.application.Application;
import javafx.embed.swing.SwingFXUtils;
import javafx.scene.Scene;
import javafx.scene.image.ImageView;
import javafx.scene.layout.StackPane;
import javafx.stage.Stage;
import java.awt.Color;
import java.awt.Graphics2D;
import java.awt.image.BufferedImage;
import com.google.zxing.BarcodeFormat;
import com.google.zxing.WriterException;
import com.google.zxing.common.BitMatrix;
import com.google.zxing.qrcode.QRCodeWriter;

public class QRCode extends Application {

@Override

public void start(Stage primaryStage) {

    QRCode qrCodeWriter = new QRCode();
    String myWeb = “http://www.yourURL.com/";
    int width = 512;
    int height = 512;
    String fileType = "png";
    BufferedImage bufferedImage = null;

    try {

        BitMatrix byteMatrix = qrCodeWriter.encode(myWeb, BarcodeFormat.QR_CODE, width, height);
        bufferedImage = new BufferedImage(width, height, BufferedImage.TYPE_INT_RGB);
        bufferedImage.createGraphics();
        Graphics2D graphics = (Graphics2D) bufferedImage.getGraphics();
        graphics.setColor(Color.WHITE);
        graphics.fillRect(0, 0, width, height);
        graphics.setColor(Color.BLACK);

            for (int i = 0; i < height; i++) {
            
                for (int j = 0; j < width; j++) {

                    if (byteMatrix.get(i, j)) {

                        graphics.fillRect(i, j, 1, 1);
                    }

                }

            }

        System.out.println(“Finished!”);

    }  catch (WriterException ex)

    {
    Logger.getLogger(ScanQRCode.class.getName()).log(Level.SEVERE, null, ex);
    }

    ImageView qrView = new ImageView();
    qrView.setImage(SwingFXUtils.toFXImage(bufferedImage, null));
    StackPane root = new StackPane();
    root.getChildren().add(qrView);
    Scene scene = new Scene(root, 350, 350);
    primaryStage.setTitle("Sample Code");
    primaryStage.setScene(scene);
    primaryStage.show();

}

public static void main(String[] args) {
    launch(args);
    }

}