from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HELPER = ROOT / "skills" / "delivery-program" / "scripts" / "delivery_program.py"


class DeliveryProgramTests(unittest.TestCase):
    def test_create_and_validate_ledger(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            ledger = Path(temporary) / "program.md"
            create = subprocess.run(
                [
                    sys.executable,
                    str(HELPER),
                    "init-ledger",
                    "--path",
                    str(ledger),
                    "--date",
                    "2026-08-18",
                    "--objective",
                    "Prove one product path",
                    "--product-proof",
                    "A focused end-to-end check passes",
                    "--acceptance-evidence",
                    "Run the focused check",
                    "--posture",
                    "exploratory",
                    "--obligation-floor",
                    "source integrity",
                    "--maturity-evidence",
                    "no current product path",
                    "--approval-gates",
                    "new architecture",
                    "--review-budget",
                    "one initial and one verification pass",
                    "--hard-limits",
                    "no new services",
                    "--tripwires",
                    "five changed files",
                ],
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(create.returncode, 0, create.stderr)
            self.assertTrue(ledger.is_file())

            validate = subprocess.run(
                [sys.executable, str(HELPER), "validate-ledger", "--path", str(ledger)],
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(validate.returncode, 0, validate.stdout + validate.stderr)

    def test_refuses_to_overwrite_ledger(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            ledger = Path(temporary) / "program.md"
            ledger.write_text("existing\n", encoding="utf-8")
            result = subprocess.run(
                [
                    sys.executable,
                    str(HELPER),
                    "init-ledger",
                    "--path",
                    str(ledger),
                    "--date",
                    "2026-08-18",
                    "--objective",
                    "Do not overwrite",
                    "--product-proof",
                    "Existing file remains",
                    "--acceptance-evidence",
                    "Read the file",
                    "--posture",
                    "exploratory",
                    "--obligation-floor",
                    "source integrity",
                    "--maturity-evidence",
                    "existing state",
                    "--approval-gates",
                    "none",
                    "--review-budget",
                    "one pass",
                    "--hard-limits",
                    "none",
                    "--tripwires",
                    "none",
                ],
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(ledger.read_text(encoding="utf-8"), "existing\n")


if __name__ == "__main__":
    unittest.main()
