from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HELPER = ROOT / "skills" / "delivery-program" / "scripts" / "delivery_program.py"


def run_helper(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(HELPER), *args],
        check=False,
        capture_output=True,
        text=True,
    )


class DeliveryProgramTests(unittest.TestCase):
    def test_create_and_validate_ledger(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            ledger = Path(temporary) / "program.md"
            create = run_helper(
                "init-ledger",
                "--path",
                str(ledger),
                "--date",
                "2026-08-18",
                "--objective",
                "Prove one product path",
                "--product-proof",
                "A focused end-to-end check passes",
                "--posture",
                "exploratory",
                "--obligation-floor",
                "source integrity",
                "--maturity-evidence",
                "no current product path",
            )
            self.assertEqual(create.returncode, 0, create.stderr)
            validate = run_helper("validate-ledger", "--path", str(ledger))
            self.assertEqual(validate.returncode, 0, validate.stdout + validate.stderr)

    def test_create_and_validate_active_slice(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            record = Path(temporary) / "slice.md"
            create = run_helper(
                "init-slice",
                "--path",
                str(record),
                "--slice-id",
                "SLICE-01",
                "--date",
                "2026-08-18",
                "--baseline",
                "abc123",
                "--product-behavior",
                "One real caller uses the successor",
                "--direct-proof",
                "Run the product path",
            )
            self.assertEqual(create.returncode, 0, create.stderr)
            validate = run_helper("validate-slice", "--path", str(record))
            self.assertEqual(validate.returncode, 0, validate.stdout + validate.stderr)

    def test_refuses_to_overwrite(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            ledger = Path(temporary) / "program.md"
            ledger.write_text("existing\n", encoding="utf-8")
            result = run_helper(
                "init-ledger",
                "--path",
                str(ledger),
                "--date",
                "2026-08-18",
                "--objective",
                "Do not overwrite",
                "--product-proof",
                "Existing file remains",
                "--posture",
                "exploratory",
                "--obligation-floor",
                "source integrity",
                "--maturity-evidence",
                "existing state",
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(ledger.read_text(encoding="utf-8"), "existing\n")

    def test_build_ready_slice_requires_authority_and_dispositions(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            record = Path(temporary) / "slice.md"
            create = run_helper(
                "init-slice",
                "--path",
                str(record),
                "--slice-id",
                "SLICE-02",
                "--date",
                "2026-08-18",
                "--baseline",
                "abc123",
                "--readiness",
                "build-ready",
                "--product-behavior",
                "Replace one runtime authority",
                "--direct-proof",
                "Run the product path",
            )
            self.assertEqual(create.returncode, 0, create.stderr)
            validate = run_helper("validate-slice", "--path", str(record))
            self.assertNotEqual(validate.returncode, 0)
            self.assertIn("no explicit authority", validate.stdout)
            self.assertIn("no responsibility disposition", validate.stdout)
            self.assertIn("no policy trace", validate.stdout)


if __name__ == "__main__":
    unittest.main()
