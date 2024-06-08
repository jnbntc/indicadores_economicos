import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.firefox.launch(headless=True)
        page = await browser.new_page()
        await page.goto('https://www.ambito.com/contenidos/riesgo-pais.html')
        await page.wait_for_selector('div.first.variation-last__data-wrapper span.variation-last__value.value.data-ultimo')

        # Extraer el valor del "riesgo país"
        riesgo_pais_value = await page.inner_text('div.first.variation-last__data-wrapper span.variation-last__value.value.data-ultimo')
        print(f'Riesgo País: {riesgo_pais_value}')

        await browser.close()

# Ejecutar la función principal de asyncio
asyncio.run(main())