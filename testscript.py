import asyncio
from random import randint
from playwright.async_api import Playwright, async_playwright
from os import path,makedirs
import time
import PIL.Image, PIL.ImageTk, PIL.ImageFont, PIL.ImageDraw, PIL.ImageOps
from io import BytesIO

jira_server = "https://YourServerAddress.com"
jira_test = "https://YourTestCloudAddress.atlassian.net/"
jira_cloud = "https://YourProdCloudAddress.atlassian.net/"

def test_view(distrib,project,number_tickets,range_high,range_low,font_path):
    distrib = distrib.replace("%20","")
    project = project.replace("%20","")
    number_tickets = number_tickets.replace("%20","")
    range_high = range_high.replace("%20","")
    range_low = range_low.replace("%20","")
    required_folder = "Macintosh HD/Users/Shared"
    list_numbers = [randint(int(range_low), int(range_high)) for i in range(1,int(number_tickets)+1,1)]

    print(font_path)
    font = PIL.ImageFont.truetype(font_path.replace("%20"," "), 36)

    y = 1

    width=950
    height=950
    array = []

    async def run(playwright: Playwright) -> None:
        browser = await playwright.chromium.launch(
            headless=False,
        )
        context = await browser.new_context(
            viewport={ 'width': width, 'height': height }
        )
        
        page1 = await context.new_page()
        await page1.goto(jira_server+"/login.jsp")
        await page1.locator('xpath=//*[@id="header-details-user-fullname"]/span/span/img').click(timeout=150000)

        adress = jira_test
        if int(distrib)== 1:
            adress = jira_cloud


        page2 = await context.new_page()
        await page2.goto(adress)
        await page2.get_by_label("Your profile and settings").click(timeout=150000)
        i = 1
        for element in list_numbers:
            ticket = str(project)+"-"+str(element)
            p1 = jira_server+"/browse/"+ticket
            p1 = p1.replace("%20","").replace(" ","")
            await page1.goto(p1)
            if i == 1:
                if await page1.locator('xpath=//*[@id="sidebar"]').get_attribute('aria-expanded') != 'false':
                    await page1.locator('xpath=//*[@id="sidebar"]/div/div[2]/button').click()
                    time.sleep(3)
            s1 = await page1.screenshot()
            p2 = adress+"browse/"+ticket
            p2 = p2.replace("%20","").replace(" ","")
            await page2.goto(p2)
            if i == 1:
                if int(distrib) == 1:
                    await page2.get_by_role("button", name="Only necessary").click()
                if await page2.locator('//*[@id="ak-side-navigation"]/div/div[1]').get_attribute('aria-hidden') == 'false':
                    await page2.locator('xpath=//*[@id="ak-side-navigation"]/div/div[2]/div[2]/button').click()
            s2 = await page2.screenshot()
            array.append([s1,s2,ticket])
            i += 1

    
        await page1.close()
        await page2.close()

        # ---------------------
        await context.close()
        await browser.close()


    async def main() -> None:
        async with async_playwright() as playwright:
            await run(playwright)


    asyncio.run(main())

    if not path.exists(required_folder+"/"+"test"):
        makedirs(required_folder+"/"+"test")
    image_list = []
    for item in array:
        im1,im2 = PIL.ImageOps.expand(PIL.Image.open(BytesIO(item[0])), border=(5,10)),PIL.ImageOps.expand(PIL.Image.open(BytesIO(item[1])), border=(5,10))
        draw1,draw2 = PIL.ImageDraw.Draw(im1),PIL.ImageDraw.Draw(im2)
        draw1.text((round(width/50),round(height/70)),"jira-server",fill=(255, 255, 255),font=font,stroke_width=2,stroke_fill=(0,0,0),)
        if int(distrib) == 0:
            draw2.text((round(width/50),round(height/70)),"cloud-sandbox",fill=(255, 255, 255),font=font,stroke_width=2,stroke_fill=(0,0,0))
        else:
            draw2.text((round(width/50),round(height/70)),"cloud-prod",fill=(255, 255, 255),font=font,stroke_width=2,stroke_fill=(0,0,0))

        dst = PIL.Image.new('RGBA', (im1.width + im2.width, im1.height))
        dst.paste(im1, (0, 0))
        dst.paste(im2, (im1.width, 0))
        #dst.save(image_io,'PNG')
        image_list.append([dst,item[2]])
        y += 1

    print(image_list)
    return image_list