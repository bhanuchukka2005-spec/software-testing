
import org.junit.Assert;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.openqa.selenium.support.ui.ExpectedConditions;

import java.time.Duration;

public class AppTest {

    WebDriver driver;

    // Setup before executing the test
    @Before
    public void setUp() {

        driver = new ChromeDriver();

        driver.manage().window().maximize();

        driver.get(
            "https://practicetestautomation.com/practice-test-login/"
        );
    }

    // Test valid login
    @Test
    public void testValidLogin() {

        // Enter username
        driver.findElement(By.id("username"))
              .sendKeys("student");

        // Enter password
        driver.findElement(By.id("password"))
              .sendKeys("Password123");

        // Click login button
        driver.findElement(By.id("submit")).click();

        // Wait for success heading
        WebDriverWait wait = new WebDriverWait(
            driver, Duration.ofSeconds(10)
        );

        WebElement heading = wait.until(
            ExpectedConditions.visibilityOfElementLocated(
                By.tagName("h1")
            )
        );

        // Validate heading
        String actualHeading = heading.getText();

        Assert.assertEquals(
            "Login heading did not match",
            "Logged In Successfully",
            actualHeading
        );

        System.out.println(
            "Login heading matched. Test Passed."
        );

        // Validate URL
        String currentURL = driver.getCurrentUrl();

        Assert.assertTrue(
            "URL validation failed",
            currentURL.contains("logged-in-successfully")
        );

        System.out.println(
            "URL validation passed. Test Passed."
        );
    }

    // Close browser after testing
    @After
    public void tearDown() {

        if (driver != null) {
            driver.quit();
        }
    }
}
