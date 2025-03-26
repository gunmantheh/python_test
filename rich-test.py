import rich
from time import sleep
import os, sys, logging
from rich.tree import Tree
from rich.table import Column
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.live import Live
from rich.panel import Panel
from rich.table import Table

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s : %(message)s')

def main():
    pid = os.getpid()
    print(f'test: {pid}')
    job_progress = Progress(
        "{task.description}",
        SpinnerColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
    )
    job1 = job_progress.add_task("[green]Cooking")
    job2 = job_progress.add_task("[magenta]Baking", total=200)
    job3 = job_progress.add_task("[cyan]Mixing", total=400)

    total = sum(task.total for task in job_progress.tasks)
    overall_progress = Progress("Overall progress", SpinnerColumn())
    overall_task = overall_progress.add_task("All Jobs", total=int(total))

    # progress_table = Table.grid()
    # progress_table.add_row(
    #     Panel.fit(
    #         overall_progress, title="Overall Progress", border_style="green", padding=(2, 2)
    #     ),
    #     Panel.fit(job_progress, title="[b]Jobs", border_style="red", padding=(1, 2)),
    # )
    rootTree = Tree("myTasks")
    rootTree.add(overall_progress)
    with Live(rootTree, refresh_per_second=10):
        while not overall_progress.finished:
            sleep(0.1)
            for job in job_progress.tasks:
                if not job.finished:
                    job_progress.advance(job.id, advance=10)

            # completed = sum(task.completed for task in job_progress.tasks)
            overall_progress.update(overall_task, advance=10)
        overall_progress.update(overall_task, description=f"{overall_progress.columns[0]} - Finished") # not working at the moment

if __name__ == "__main__":
    logger.info('Started')
    main()
    logger.info('Finished')