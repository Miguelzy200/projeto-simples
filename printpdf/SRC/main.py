import asyncio
import pypdf

async def random_print():
    print("Hello World!")


async def read_pdf(path):
    pdfBin = open(path, "rb")
    pdfRead = pypdf.PdfReader(pdfBin)
    pdfContent = ""
    for pageIndex in range(pdfRead.get_num_pages()):
        page = pdfRead.get_page(pageIndex)
        text = page.extract_text().replace("\n", " ")
        pdfContent += f"\nPágina: {pageIndex + 1}\nTexto: {text}\n"
    print(pdfContent)


async def main():
    task1 = asyncio.create_task(random_print())
    task2 = asyncio.create_task(read_pdf("PdfTeste.pdf"))

    await task1
    await task2


asyncio.run(main()) 