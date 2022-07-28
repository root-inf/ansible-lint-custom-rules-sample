from typing import Any, Dict

from ansiblelint.rules import AnsibleLintRule


class UseLoopInsteadOfWithRule(AnsibleLintRule):
    id = "use-loop"
    shortdesc = "繰り返し表現には with_* ではなく loop 記法を使用"
    description = (
        "Playbook中の繰り返し表現には公式推奨である loop 記法を使用 抽出条件は公式ドキュメントに変換例があるもの\n"
        "https://docs.ansible.com/ansible/latest/user_guide/playbooks_loops.html"
        "#migrating-from-with-x-to-loop"
    )
    severity = "MEDIUM"
    tags = ["must"]
    version_added = "v1.0.0"

    _with_xs = {
        "with_list",
        "with_items",
        "with_indexed_items",
        "with_flattened",
        "with_together",
        "with_dict",
        "with_sequence",
        "with_subelements",
        "with_nested",
        "with_cartesian",
        "with_random_choice",
    }

    def matchtask(self, task: Dict[str, Any]) -> bool:
        # task.keys()と_with_xsの積集合でtask内にwith_Xがあるかどうか判定
        if task.keys() & self._with_xs:
            return True
        return False
