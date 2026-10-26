"""Build build/Pipeline.xlsx (import into Google Sheets: File > Import > Upload)."""
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill
from openpyxl.worksheet.datavalidation import DataValidation

TABS = {
    "prospects": ["date_added", "business", "website", "city", "niche", "contact_name", "contact_role",
                  "contact_route", "observation", "source_url", "status", "emailed_on", "touch",
                  "last_reply_on", "notes"],
    "clients": ["client", "niche", "city", "icp_notes", "start_date", "sheet_url", "price", "status",
                "last_delivered", "wins_reported"],
    "weekly": ["week_of", "prospects_added", "emails_sent", "replies", "samples", "won", "lost",
               "opt_outs", "mrr", "dollars_per_hour", "median_zerogpt"],
    "suppression": ["email_or_domain", "reason", "date"],
}
DROPDOWNS = {
    ("prospects", "status"): "new,emailed,replied,sample_sent,won,lost,nurture",
    ("prospects", "touch"): "1,2,3",
    ("clients", "status"): "active,paused,cancelled",
    ("suppression", "reason"): "opt-out,bounce,not interested,other",
}
ROWS = 2000

wb = Workbook()
wb.remove(wb.active)
for name, headers in TABS.items():
    ws = wb.create_sheet(name)
    ws.append(headers)
    for cell in ws[1]:
        cell.font = Font(bold=True, color="FFFFFF")
        cell.fill = PatternFill("solid", fgColor="1F4E79")
    ws.freeze_panes = "A2"
    for i, h in enumerate(headers, start=1):
        ws.column_dimensions[ws.cell(1, i).column_letter].width = max(12, len(h) + 4)
    for (tab, col), values in DROPDOWNS.items():
        if tab == name:
            letter = ws.cell(1, headers.index(col) + 1).column_letter
            dv = DataValidation(type="list", formula1=f'"{values}"', allow_blank=True)
            ws.add_data_validation(dv)
            dv.add(f"{letter}2:{letter}{ROWS}")

# $/hr = MRR / 720 hours in a 30-day month
ws = wb["weekly"]
for r in range(2, 200):
    ws[f"J{r}"] = f'=IF(I{r}="","",ROUND(I{r}/720,2))'

out = Path(__file__).resolve().parent.parent / "build" / "Pipeline.xlsx"
out.parent.mkdir(exist_ok=True)
wb.save(out)
print(out)
