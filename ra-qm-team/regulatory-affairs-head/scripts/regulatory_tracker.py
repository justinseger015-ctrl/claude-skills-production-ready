#!/usr/bin/env python3
"""
Regulatory Submission Tracking System
Automates monitoring and reporting of regulatory submission status.

This script tracks regulatory submissions and generates comprehensive
compliance reports. Supports both text (human-readable) and JSON output
for integration with compliance dashboards.

Usage:
    python regulatory_tracker.py regulatory_submissions.json
    python regulatory_tracker.py data.json --output json
    python regulatory_tracker.py data.json -o json -f results.json
    python regulatory_tracker.py data.json -o text -v

Author: Regulatory Affairs Team
Version: 2.0.0
Last Updated: 2025-11-05
"""

import argparse
import json
import sys
import datetime
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict
from enum import Enum
from pathlib import Path

class SubmissionType(Enum):
    FDA_510K = "FDA_510K"
    FDA_PMA = "FDA_PMA"
    FDA_DE_NOVO = "FDA_DE_NOVO"
    EU_MDR_CE = "EU_MDR_CE"
    ISO_CERTIFICATION = "ISO_CERTIFICATION"
    GLOBAL_REGULATORY = "GLOBAL_REGULATORY"

class SubmissionStatus(Enum):
    PLANNING = "PLANNING"
    IN_PREPARATION = "IN_PREPARATION"
    SUBMITTED = "SUBMITTED"
    UNDER_REVIEW = "UNDER_REVIEW"
    ADDITIONAL_INFO_REQUESTED = "ADDITIONAL_INFO_REQUESTED"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    WITHDRAWN = "WITHDRAWN"

@dataclass
class RegulatorySubmission:
    submission_id: str
    product_name: str
    submission_type: SubmissionType
    submission_status: SubmissionStatus
    target_market: str
    submission_date: Optional[datetime.date] = None
    target_approval_date: Optional[datetime.date] = None
    actual_approval_date: Optional[datetime.date] = None
    regulatory_authority: str = ""
    responsible_person: str = ""
    notes: str = ""
    last_updated: datetime.date = datetime.date.today()

class RegulatoryTracker:
    def __init__(self, data_file: str = "regulatory_submissions.json"):
        self.data_file = data_file
        self.submissions: Dict[str, RegulatorySubmission] = {}
        self.load_data()
    
    def load_data(self):
        """Load existing submission data from JSON file"""
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                for sub_id, sub_data in data.items():
                    # Convert date strings back to date objects
                    for date_field in ['submission_date', 'target_approval_date', 
                                     'actual_approval_date', 'last_updated']:
                        if sub_data.get(date_field):
                            sub_data[date_field] = datetime.datetime.strptime(
                                sub_data[date_field], '%Y-%m-%d').date()
                    
                    # Convert enums
                    sub_data['submission_type'] = SubmissionType(sub_data['submission_type'])
                    sub_data['submission_status'] = SubmissionStatus(sub_data['submission_status'])
                    
                    self.submissions[sub_id] = RegulatorySubmission(**sub_data)
        except FileNotFoundError:
            print(f"No existing data file found. Starting fresh.")
        except Exception as e:
            print(f"Error loading data: {e}")
    
    def save_data(self):
        """Save submission data to JSON file"""
        data = {}
        for sub_id, submission in self.submissions.items():
            sub_dict = asdict(submission)
            # Convert date objects to strings
            for date_field in ['submission_date', 'target_approval_date', 
                             'actual_approval_date', 'last_updated']:
                if sub_dict.get(date_field):
                    sub_dict[date_field] = sub_dict[date_field].strftime('%Y-%m-%d')
            
            # Convert enums to strings
            sub_dict['submission_type'] = sub_dict['submission_type'].value
            sub_dict['submission_status'] = sub_dict['submission_status'].value
            
            data[sub_id] = sub_dict
        
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=2)
    
    def add_submission(self, submission: RegulatorySubmission):
        """Add new regulatory submission"""
        self.submissions[submission.submission_id] = submission
        self.save_data()
        print(f"Added submission: {submission.submission_id}")
    
    def update_submission_status(self, submission_id: str, 
                               new_status: SubmissionStatus, 
                               notes: str = ""):
        """Update submission status"""
        if submission_id in self.submissions:
            self.submissions[submission_id].submission_status = new_status
            self.submissions[submission_id].notes = notes
            self.submissions[submission_id].last_updated = datetime.date.today()
            self.save_data()
            print(f"Updated {submission_id} status to {new_status.value}")
        else:
            print(f"Submission {submission_id} not found")
    
    def get_submissions_by_status(self, status: SubmissionStatus) -> List[RegulatorySubmission]:
        """Get all submissions with specific status"""
        return [sub for sub in self.submissions.values() if sub.submission_status == status]
    
    def get_overdue_submissions(self) -> List[RegulatorySubmission]:
        """Get submissions that are overdue"""
        today = datetime.date.today()
        overdue = []
        for submission in self.submissions.values():
            if (submission.target_approval_date and 
                submission.target_approval_date < today and 
                submission.submission_status not in [SubmissionStatus.APPROVED, 
                                                   SubmissionStatus.REJECTED, 
                                                   SubmissionStatus.WITHDRAWN]):
                overdue.append(submission)
        return overdue
    
    def generate_status_report(self) -> str:
        """Generate comprehensive status report as human-readable text"""
        report = []
        report.append("REGULATORY SUBMISSION STATUS REPORT")
        report.append("=" * 50)
        report.append(f"Generated: {datetime.date.today()}")
        report.append("")

        # Summary by status
        status_counts = {}
        for status in SubmissionStatus:
            count = len(self.get_submissions_by_status(status))
            if count > 0:
                status_counts[status] = count

        report.append("SUBMISSION STATUS SUMMARY:")
        for status, count in status_counts.items():
            report.append(f"  {status.value}: {count}")
        report.append("")

        # Overdue submissions
        overdue = self.get_overdue_submissions()
        if overdue:
            report.append("OVERDUE SUBMISSIONS:")
            for submission in overdue:
                days_overdue = (datetime.date.today() - submission.target_approval_date).days
                report.append(f"  {submission.submission_id} - {days_overdue} days overdue")
            report.append("")

        # Active submissions requiring attention
        active_statuses = [SubmissionStatus.SUBMITTED, SubmissionStatus.UNDER_REVIEW,
                          SubmissionStatus.ADDITIONAL_INFO_REQUESTED]
        active_submissions = []
        for status in active_statuses:
            active_submissions.extend(self.get_submissions_by_status(status))

        if active_submissions:
            report.append("ACTIVE SUBMISSIONS REQUIRING ATTENTION:")
            for submission in active_submissions:
                report.append(f"  {submission.submission_id} - {submission.product_name}")
                report.append(f"    Status: {submission.submission_status.value}")
                report.append(f"    Target Date: {submission.target_approval_date}")
                report.append(f"    Authority: {submission.regulatory_authority}")
                report.append("")

        return "\n".join(report)

    def generate_json_report(self, verbose: bool = False) -> Dict[str, Any]:
        """Generate comprehensive status report as structured JSON"""
        # Summary by status
        status_counts = {}
        for status in SubmissionStatus:
            submissions = self.get_submissions_by_status(status)
            if len(submissions) > 0:
                status_counts[status.value] = len(submissions)

        # Overdue submissions
        overdue = self.get_overdue_submissions()
        overdue_data = []
        for submission in overdue:
            days_overdue = (datetime.date.today() - submission.target_approval_date).days
            overdue_data.append({
                "submission_id": submission.submission_id,
                "product_name": submission.product_name,
                "days_overdue": days_overdue,
                "target_date": submission.target_approval_date.strftime('%Y-%m-%d') if submission.target_approval_date else None
            })

        # Active submissions
        active_statuses = [SubmissionStatus.SUBMITTED, SubmissionStatus.UNDER_REVIEW,
                          SubmissionStatus.ADDITIONAL_INFO_REQUESTED]
        active_submissions = []
        for status in active_statuses:
            active_submissions.extend(self.get_submissions_by_status(status))

        active_data = []
        for submission in active_submissions:
            active_data.append({
                "submission_id": submission.submission_id,
                "product_name": submission.product_name,
                "status": submission.submission_status.value,
                "submission_type": submission.submission_type.value,
                "target_date": submission.target_approval_date.strftime('%Y-%m-%d') if submission.target_approval_date else None,
                "regulatory_authority": submission.regulatory_authority,
                "target_market": submission.target_market
            })

        # All submissions (verbose only)
        all_submissions = []
        if verbose:
            for sub_id, submission in self.submissions.items():
                sub_dict = asdict(submission)
                # Convert dates to strings
                for date_field in ['submission_date', 'target_approval_date', 'actual_approval_date', 'last_updated']:
                    if sub_dict.get(date_field):
                        sub_dict[date_field] = sub_dict[date_field].strftime('%Y-%m-%d')
                # Convert enums to strings
                sub_dict['submission_type'] = sub_dict['submission_type'].value
                sub_dict['submission_status'] = sub_dict['submission_status'].value
                all_submissions.append(sub_dict)

        report = {
            "metadata": {
                "tool": "regulatory_tracker.py",
                "version": "2.0.0",
                "timestamp": datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
                "generated_date": datetime.date.today().strftime('%Y-%m-%d')
            },
            "summary": {
                "total_submissions": len(self.submissions),
                "status_summary": status_counts,
                "overdue_count": len(overdue)
            },
            "results": {
                "overdue_submissions": overdue_data,
                "active_submissions": active_data
            }
        }

        if verbose:
            report["results"]["all_submissions"] = all_submissions

        return report

def main():
    """
    Main entry point with standardized argument parsing.

    Parses command-line arguments, validates input, loads regulatory data,
    generates compliance reports, and writes output in the specified format.
    """
    parser = argparse.ArgumentParser(
        description='Track regulatory submissions and generate compliance reports for HealthTech/MedTech products',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate text report (default)
  %(prog)s regulatory_submissions.json

  # Generate JSON report for compliance dashboard
  %(prog)s regulatory_submissions.json --output json

  # Save JSON report to file with verbose details
  %(prog)s regulatory_submissions.json -o json -f dashboard_report.json -v

  # Generate text report with verbose regulatory authority details
  %(prog)s regulatory_submissions.json --verbose

For more information, see the skill documentation at:
ra-qm-team/regulatory-affairs-head/SKILL.md
        """
    )

    # Positional arguments
    parser.add_argument(
        'input',
        help='Regulatory submissions JSON data file'
    )

    # Optional arguments
    parser.add_argument(
        '--output', '-o',
        choices=['text', 'json'],
        default='text',
        help='Output format: text (default) for human reading, json for dashboard integration'
    )

    parser.add_argument(
        '--file', '-f',
        help='Write output to file instead of stdout'
    )

    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose output: detailed compliance info and all submission details'
    )

    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s 2.0.0'
    )

    # Parse arguments
    args = parser.parse_args()

    try:
        # Validate input file
        input_path = Path(args.input)

        if not input_path.exists():
            print(f"Error: Input file not found: {args.input}", file=sys.stderr)
            sys.exit(1)

        if not input_path.is_file():
            print(f"Error: Path is not a file: {args.input}", file=sys.stderr)
            sys.exit(1)

        # Load regulatory tracker
        if args.verbose:
            print(f"Loading regulatory data from: {args.input}", file=sys.stderr)

        tracker = RegulatoryTracker(str(input_path))

        if args.verbose:
            print(f"Loaded {len(tracker.submissions)} submissions", file=sys.stderr)

        # Generate report based on output format
        if args.output == 'json':
            report_data = tracker.generate_json_report(verbose=args.verbose)
            output = json.dumps(report_data, indent=2)
        else:  # text (default)
            output = tracker.generate_status_report()

            # Add verbose regulatory authority details if requested
            if args.verbose and len(tracker.submissions) > 0:
                output += "\n\n--- DETAILED SUBMISSION INFORMATION ---\n"
                for sub_id, submission in tracker.submissions.items():
                    output += f"\nSubmission ID: {sub_id}\n"
                    output += f"Product: {submission.product_name}\n"
                    output += f"Type: {submission.submission_type.value}\n"
                    output += f"Status: {submission.submission_status.value}\n"
                    output += f"Market: {submission.target_market}\n"
                    output += f"Authority: {submission.regulatory_authority}\n"
                    output += f"Responsible: {submission.responsible_person}\n"
                    output += f"Submission Date: {submission.submission_date}\n"
                    output += f"Target Approval: {submission.target_approval_date}\n"
                    output += f"Actual Approval: {submission.actual_approval_date}\n"
                    if submission.notes:
                        output += f"Notes: {submission.notes}\n"

        # Write output to file or stdout
        if args.file:
            try:
                output_path = Path(args.file)
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(output)

                if args.verbose:
                    print(f"Report written to: {args.file}", file=sys.stderr)
                else:
                    print(f"Report saved to: {args.file}")

            except PermissionError:
                print(f"Error: Permission denied writing to: {args.file}", file=sys.stderr)
                sys.exit(4)
            except Exception as e:
                print(f"Error writing output file: {e}", file=sys.stderr)
                sys.exit(4)
        else:
            # Print to stdout
            print(output)

        # Success
        sys.exit(0)

    except FileNotFoundError as e:
        print(f"Error: File not found: {e}", file=sys.stderr)
        sys.exit(1)

    except PermissionError as e:
        print(f"Error: Permission denied: {e}", file=sys.stderr)
        sys.exit(1)

    except ValueError as e:
        print(f"Error: Invalid input data: {e}", file=sys.stderr)
        sys.exit(3)

    except KeyboardInterrupt:
        print("\nOperation cancelled by user", file=sys.stderr)
        sys.exit(130)

    except Exception as e:
        print(f"Error: Unexpected error occurred: {e}", file=sys.stderr)
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
