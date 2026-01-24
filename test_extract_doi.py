from pathlib import Path

from database.text_processor import TextProcessor


def main() -> int:
    base_dir = Path(__file__).resolve().parent
    raw_dir = base_dir / "data" / "raw" / "O5H"
    if not raw_dir.exists():
        print(f"Directory not found: {raw_dir}")
        return 1

    processor = TextProcessor(data_dir=str(base_dir / "data" / "raw"))

    results = []
    unknowns = []
    for md_file in sorted(raw_dir.glob("*.md")):
        content = md_file.read_text(encoding="utf-8", errors="ignore")
        doi = processor.extract_doi_from_content(content, md_file.name, str(md_file))
        results.append((md_file.name, doi))
        
        if doi == "unknown":
            # Extract first # title for debugging
            title_line = ""
            for line in content.splitlines():
                if line.strip().startswith("#"):
                    title_line = line.strip().lstrip("#").strip()
                    break
            unknowns.append((md_file.name, title_line))
            print(f"❌ {md_file.name}")
            print(f"   Title: {title_line[:80]}...")
        else:
            print(f"✓ {md_file.name}\t{doi}")

    total = len(results)
    unknown = len(unknowns)
    print(f"\n{'='*60}")
    print(f"Total: {total}, Unknown: {unknown}")
    
    if unknowns:
        print(f"\n❌ Failed files:")
        for fname, title in unknowns:
            print(f"  - {fname}")
            print(f"    Title: {title[:80]}")
    
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
