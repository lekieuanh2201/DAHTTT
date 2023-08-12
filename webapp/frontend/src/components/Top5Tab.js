import React from "react";

import Tabs from "./Tabs";
import Panel from "./Panel";
import TopComment from "./TopComment";
import TopLike from "./TopLike";

function Top5Tab() {
  return (
    <Tabs>
      <Panel title="Most Comments">
        <TopComment/>
      </Panel>
      <Panel title="Most likes">
        <TopLike />
      </Panel>
    </Tabs>
  );
}
export default Top5Tab;
