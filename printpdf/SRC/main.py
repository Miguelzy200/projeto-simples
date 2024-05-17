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


async def run():
    pdfPath = input("Insira o caminho completo do pdf: ")
    task1 = asyncio.create_task(random_print())
    task2 = asyncio.create_task(read_pdf(pdfPath))

    await task1
    await task2


def main() -> None:
    asyncio.run(run())


if __name__ == '__main__':
    main()