### useUnload (task/1)

#### canonical solution

```javascript
const useUnload = fn => {
  const cb = React.useRef(fn);

  React.useEffect(() => {
    const onUnload = cb.current;
    window.addEventListener('beforeunload', onUnload);
    return () => {
      window.removeEventListener('beforeunload', onUnload);
    };
  }, [cb]);
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,11 +1,10 @@

 const useUnload = fn => {
-  const cb = React.useRef(fn);
+  useEffect(() => {
+    window.addEventListener('beforeunload', fn);
+    return () => {
+      window.removeEventListener('beforeunload', fn);
+    };
+  }, [fn]);
+};
 
-  React.useEffect(() => {
-    const onUnload = cb.current;
-    window.addEventListener('beforeunload', onUnload);
-    return () => {
-      window.removeEventListener('beforeunload', onUnload);
-    };
-  }, [cb]);
-};
+export default useUnload;
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,11 +1,11 @@

 const useUnload = fn => {
-  const cb = React.useRef(fn);
+  const unload = function() {
+    if (typeof fn === 'function') {
+      fn();
+    }
+  };
+  window.addEventListener('beforeunload', unload);
+  return unload;
+};
 
-  React.useEffect(() => {
-    const onUnload = cb.current;
-    window.addEventListener('beforeunload', onUnload);
-    return () => {
-      window.removeEventListener('beforeunload', onUnload);
-    };
-  }, [cb]);
-};
+export default useUnload;
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,11 +1,16 @@

 const useUnload = fn => {
-  const cb = React.useRef(fn);
+  if (useCallback) {
+    return useCallback(fn, [])
+  }
 
-  React.useEffect(() => {
-    const onUnload = cb.current;
-    window.addEventListener('beforeunload', onUnload);
+  const listener = useRef()
+  listener.current = fn
+
+  useEffect(() => {
     return () => {
-      window.removeEventListener('beforeunload', onUnload);
-    };
-  }, [cb]);
-};
+      window.removeEventListener('beforeunload', listener.current)
+    }
+  }, [])
+
+  useEffect(() => {
+    window.addEventListener('beforeunload', listener.current)
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,11 +1,14 @@

 const useUnload = fn => {
-  const cb = React.useRef(fn);
+  return useCallback(() => {
+    if (typeof fn === 'function') {
+      fn();
+    }
+  }, [fn]);
+};
 
-  React.useEffect(() => {
-    const onUnload = cb.current;
-    window.addEventListener('beforeunload', onUnload);
+const useDocumentTitle = (title: string) => {
+  const { current: initialTitle } = useRef(document.title);
+  useEffect(() => {
+    document.title = title;
     return () => {
-      window.removeEventListener('beforeunload', onUnload);
-    };
-  }, [cb]);
-};
+      document.title = initialTitle;
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,11 +1,14 @@

 const useUnload = fn => {
-  const cb = React.useRef(fn);
+    const fnName = Symbol(fn.name);
+    window.addEventListener('beforeunload', ev => {
+        if (typeof fn === 'function') {
+            fn();
+        }
+        if (ev.target === window) {
+            ev.returnValue = true;
+        }
+    });
+    return fnName;
+};
 
-  React.useEffect(() => {
-    const onUnload = cb.current;
-    window.addEventListener('beforeunload', onUnload);
-    return () => {
-      window.removeEventListener('beforeunload', onUnload);
-    };
-  }, [cb]);
-};
+export default useUnload;
```

### useClickOutside (task/2)

#### canonical solution

```javascript
const useClickOutside = (ref, callback) => {
  const handleClick = e => {
    if (ref.current && !ref.current.contains(e.target)) {
      callback();
    }
  };
  React.useEffect(() => {
    document.addEventListener('click', handleClick);
    return () => {
      document.removeEventListener('click', handleClick);
    };
  });
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,13 +1,17 @@

 const useClickOutside = (ref, callback) => {
-  const handleClick = e => {
+  const handleClick = (e) => {
     if (ref.current && !ref.current.contains(e.target)) {
       callback();
     }
   };
-  React.useEffect(() => {
+
+  useEffect(() => {
     document.addEventListener('click', handleClick);
+
     return () => {
       document.removeEventListener('click', handleClick);
     };
   });
 };
+
+const DropdownMenu = ({ children
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,13 +1,16 @@

 const useClickOutside = (ref, callback) => {
-  const handleClick = e => {
-    if (ref.current && !ref.current.contains(e.target)) {
+  const handleClick = event => {
+    if (ref.current && !ref.current.contains(event.target)) {
       callback();
     }
   };
-  React.useEffect(() => {
-    document.addEventListener('click', handleClick);
+
+  useEffect(() => {
+    document.addEventListener("mousedown", handleClick);
     return () => {
-      document.removeEventListener('click', handleClick);
+      document.removeEventListener("mousedown", handleClick);
     };
   });
 };
+
+const useCheckbox =
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,13 +1,17 @@

 const useClickOutside = (ref, callback) => {
-  const handleClick = e => {
+  const handleClick = (e) => {
     if (ref.current && !ref.current.contains(e.target)) {
       callback();
     }
   };
-  React.useEffect(() => {
+
+  useEffect(() => {
     document.addEventListener('click', handleClick);
+
     return () => {
       document.removeEventListener('click', handleClick);
     };
   });
 };
+
+const useModal = (initial
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,13 +1,13 @@

 const useClickOutside = (ref, callback) => {
-  const handleClick = e => {
-    if (ref.current && !ref.current.contains(e.target)) {
-      callback();
-    }
-  };
-  React.useEffect(() => {
-    document.addEventListener('click', handleClick);
-    return () => {
-      document.removeEventListener('click', handleClick);
-    };
-  });
-};
+    useEffect(() => {
+        const handleClickOutside = (event) => {
+            if (ref.current && !ref.current.contains(event.target)) {
+                callback();
+            }
+        };
+
+        document.addEventListener('mousedown', handleClickOutside);
+        return () => {
+            document.removeEventListener('mousedown', handleClickOutside);
+        };
+    }, [ref, callback
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,13 +1,17 @@

 const useClickOutside = (ref, callback) => {
-  const handleClick = e => {
-    if (ref.current && !ref.current.contains(e.target)) {
-      callback();
-    }
-  };
-  React.useEffect(() => {
-    document.addEventListener('click', handleClick);
-    return () => {
-      document.removeEventListener('click', handleClick);
+    const handleClick = (e) => {
+        if (ref.current && !ref.current.contains(e.target)) {
+            callback();
+        }
     };
-  });
+
+    useEffect(() => {
+        document.addEventListener('click', handleClick);
+
+        return () => {
+            document.removeEventListener('click', handleClick);
+        };
+    });
 };
+
+export default useClickOutside;
```

### useSessionStorage (task/3)

#### canonical solution

```javascript
const useSessionStorage = (keyName, defaultValue) => {
  const [storedValue, setStoredValue] = React.useState(() => {
    try {
      const value = window.sessionStorage.getItem(keyName);

      if (value) {
        return JSON.parse(value);
      } else {
        window.sessionStorage.setItem(keyName, JSON.stringify(defaultValue));
        return defaultValue;
      }
    } catch (err) {
      return defaultValue;
    }
  });

  const setValue = newValue => {
    try {
      window.sessionStorage.setItem(keyName, JSON.stringify(newValue));
    } catch (err) {}
    setStoredValue(newValue);
  };

  return [storedValue, setValue];
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,25 +1,13 @@

 const useSessionStorage = (keyName, defaultValue) => {
-  const [storedValue, setStoredValue] = React.useState(() => {
+  const [value, setValue] = useState(() => {
     try {
-      const value = window.sessionStorage.getItem(keyName);
-
-      if (value) {
-        return JSON.parse(value);
-      } else {
-        window.sessionStorage.setItem(keyName, JSON.stringify(defaultValue));
-        return defaultValue;
-      }
-    } catch (err) {
+      const value = JSON.parse(window.sessionStorage.getItem(keyName));
+      if (value) return value;
+      return defaultValue;
+    } catch (error) {
       return defaultValue;
     }
   });
 
-  const setValue = newValue => {
-    try {
-      window.sessionStorage.setItem(keyName, JSON.stringify(newValue));
-    } catch (err) {}
-    setStoredValue(newValue);
-  };
-
-  return [storedValue, setValue];
-};
+  const setSessionStorage = value => {
+    window.sessionStorage.setItem(keyName, JSON
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,25 +1,15 @@

 const useSessionStorage = (keyName, defaultValue) => {
-  const [storedValue, setStoredValue] = React.useState(() => {
-    try {
-      const value = window.sessionStorage.getItem(keyName);
+  const storedValue = sessionStorage.getItem(keyName);
+  if (storedValue) {
+    return JSON.parse(storedValue);
+  }
+  return defaultValue;
+};
 
-      if (value) {
-        return JSON.parse(value);
-      } else {
-        window.sessionStorage.setItem(keyName, JSON.stringify(defaultValue));
-        return defaultValue;
-      }
-    } catch (err) {
-      return defaultValue;
-    }
-  });
+export const storeToSessionStorage = (keyName, value) => {
+  if (value) {
+    sessionStorage.setItem(keyName, JSON.stringify(value));
+  }
+};
 
-  const setValue = newValue => {
-    try {
-      window.sessionStorage.setItem(keyName, JSON.stringify(newValue));
-    } catch (err) {}
-    setStoredValue(newValue);
-  };
-
-  return [storedValue, setValue];
-};
+export const useM
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,25 +1,13 @@

 const useSessionStorage = (keyName, defaultValue) => {
-  const [storedValue, setStoredValue] = React.useState(() => {
-    try {
-      const value = window.sessionStorage.getItem(keyName);
-
-      if (value) {
-        return JSON.parse(value);
-      } else {
-        window.sessionStorage.setItem(keyName, JSON.stringify(defaultValue));
-        return defaultValue;
-      }
-    } catch (err) {
-      return defaultValue;
-    }
-  });
-
-  const setValue = newValue => {
-    try {
-      window.sessionStorage.setItem(keyName, JSON.stringify(newValue));
-    } catch (err) {}
-    setStoredValue(newValue);
+  return {
+    setItem: (value) => {
+      window.sessionStorage.setItem(keyName, JSON.stringify(value));
+    },
+    getItem: () => {
+      return JSON.parse(window.sessionStorage.getItem(keyName) || defaultValue);
+    },
+    removeItem: () => {
+      window.sessionStorage.removeItem(keyName);
+    },
   };
-
-  return [storedValue, setValue];
 };
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,25 +1,14 @@

 const useSessionStorage = (keyName, defaultValue) => {
-  const [storedValue, setStoredValue] = React.useState(() => {
-    try {
-      const value = window.sessionStorage.getItem(keyName);
-
-      if (value) {
-        return JSON.parse(value);
-      } else {
-        window.sessionStorage.setItem(keyName, JSON.stringify(defaultValue));
-        return defaultValue;
-      }
-    } catch (err) {
-      return defaultValue;
-    }
-  });
-
-  const setValue = newValue => {
-    try {
-      window.sessionStorage.setItem(keyName, JSON.stringify(newValue));
-    } catch (err) {}
-    setStoredValue(newValue);
+  const getFromStorage = () => {
+    const item = window.sessionStorage.getItem(keyName);
+    return item ? JSON.parse(item) : defaultValue;
   };
 
-  return [storedValue, setValue];
+  const setToStorage = (value) => {
+    window.sessionStorage.setItem(keyName, JSON.stringify(value));
+  };
+
+  return [getFromStorage, setToStorage];
 };
+
+export default useSession
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,25 +1,12 @@

 const useSessionStorage = (keyName, defaultValue) => {
-  const [storedValue, setStoredValue] = React.useState(() => {
-    try {
-      const value = window.sessionStorage.getItem(keyName);
-
-      if (value) {
-        return JSON.parse(value);
-      } else {
-        window.sessionStorage.setItem(keyName, JSON.stringify(defaultValue));
-        return defaultValue;
-      }
-    } catch (err) {
-      return defaultValue;
-    }
+  const [value, setValue] = useState(() => {
+    const value = localStorage.getItem(keyName);
+    return value !== null ? JSON.parse(value) : defaultValue;
   });
 
-  const setValue = newValue => {
-    try {
-      window.sessionStorage.setItem(keyName, JSON.stringify(newValue));
-    } catch (err) {}
-    setStoredValue(newValue);
+  const setValueStorage = (value) => {
+    setValue(value);
+    localStorage.setItem(keyName, JSON.stringify(value));
   };
 
-  return [storedValue, setValue];
-};
+  return [value, setValue
```

### useTitle (task/4)

#### canonical solution

```javascript
const useTitle = title => {
  const documentDefined = typeof document !== 'undefined';
  const originalTitle = React.useRef(documentDefined ? document.title : null);

  React.useEffect(() => {
    if (!documentDefined) return;

    if (document.title !== title) document.title = title;

    return () => {
      document.title = originalTitle.current;
    };
  }, []);
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,14 +1,9 @@

 const useTitle = title => {
-  const documentDefined = typeof document !== 'undefined';
-  const originalTitle = React.useRef(documentDefined ? document.title : null);
+  useEffect(() => {
+    if (title) {
+      document.title = title;
+    }
+  }, [title]);
+};
 
-  React.useEffect(() => {
-    if (!documentDefined) return;
-
-    if (document.title !== title) document.title = title;
-
-    return () => {
-      document.title = originalTitle.current;
-    };
-  }, []);
-};
+export default useTitle;
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,14 +1,7 @@

 const useTitle = title => {
-  const documentDefined = typeof document !== 'undefined';
-  const originalTitle = React.useRef(documentDefined ? document.title : null);
+  useEffect(() => {
+    document.title = title;
+  }, [title]);
+};
 
-  React.useEffect(() => {
-    if (!documentDefined) return;
-
-    if (document.title !== title) document.title = title;
-
-    return () => {
-      document.title = originalTitle.current;
-    };
-  }, []);
-};
+export default useTitle;
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,14 +1,15 @@

 const useTitle = title => {
-  const documentDefined = typeof document !== 'undefined';
-  const originalTitle = React.useRef(documentDefined ? document.title : null);
+  const [state, setState] = useState(title);
+  const updateTitle = useCallback(
+    newTitle => {
+      setState(newTitle);
+    },
+    [setState]
+  );
+  return [state, updateTitle];
+};
 
-  React.useEffect(() => {
-    if (!documentDefined) return;
-
-    if (document.title !== title) document.title = title;
-
-    return () => {
-      document.title = originalTitle.current;
-    };
-  }, []);
-};
+const TitleHooks = () => {
+  const [title, updateTitle] = useTitle('Hello Hooks');
+  useEffect(() => {
+    document
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,14 +1,10 @@

 const useTitle = title => {
-  const documentDefined = typeof document !== 'undefined';
-  const originalTitle = React.useRef(documentDefined ? document.title : null);
+  const [titleState, setTitle] = useState(title);
+  const updateTitle = title => {
+    setTitle(title);
+    document.title = title;
+  };
+  return [titleState, updateTitle];
+};
 
-  React.useEffect(() => {
-    if (!documentDefined) return;
-
-    if (document.title !== title) document.title = title;
-
-    return () => {
-      document.title = originalTitle.current;
-    };
-  }, []);
-};
+export default useTitle;
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,14 +1,16 @@

 const useTitle = title => {
-  const documentDefined = typeof document !== 'undefined';
-  const originalTitle = React.useRef(documentDefined ? document.title : null);
+  const htmlTitle = useRef(document.title);
+  useEffect(() => {
+    document.title = title;
+    return () => {
+      document.title = htmlTitle.current;
+    };
+  }, [title]);
+};
 
-  React.useEffect(() => {
-    if (!documentDefined) return;
+const Title = ({ title }) => {
+  useTitle(title);
+  return null;
+};
 
-    if (document.title !== title) document.title = title;
-
-    return () => {
-      document.title = originalTitle.current;
-    };
-  }, []);
-};
+export default Title;
```

### useEffectOnce (task/5)

#### canonical solution

```javascript
const useEffectOnce = (callback, when) => {
  const hasRunOnce = React.useRef(false);
  React.useEffect(() => {
    if (when && !hasRunOnce.current) {
      callback();
      hasRunOnce.current = true;
    }
  }, [when]);
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,9 +1,5 @@

 const useEffectOnce = (callback, when) => {
-  const hasRunOnce = React.useRef(false);
-  React.useEffect(() => {
-    if (when && !hasRunOnce.current) {
-      callback();
-      hasRunOnce.current = true;
-    }
-  }, [when]);
+    useEffect(callback, [when]);
 };
+
+export default useEffectOnce;
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,9 +1,5 @@

 const useEffectOnce = (callback, when) => {
-  const hasRunOnce = React.useRef(false);
-  React.useEffect(() => {
-    if (when && !hasRunOnce.current) {
-      callback();
-      hasRunOnce.current = true;
-    }
-  }, [when]);
+  useEffect(callback, [when]);
 };
+
+export default useEffectOnce;
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,9 +1,13 @@

 const useEffectOnce = (callback, when) => {
-  const hasRunOnce = React.useRef(false);
-  React.useEffect(() => {
-    if (when && !hasRunOnce.current) {
-      callback();
-      hasRunOnce.current = true;
-    }
-  }, [when]);
+  const ran = useRef(false);
+  useEffect(() => {
+    if (ran.current) return;
+    ran.current = true;
+    return callback();
+  }, when);
 };
+
+const useMappedState = (mapState, mapActions) => {
+  const store = useContext(context);
+  const state = useCallback(mapState(store.state), [store.state]);
+  const
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,9 +1,14 @@

 const useEffectOnce = (callback, when) => {
-  const hasRunOnce = React.useRef(false);
-  React.useEffect(() => {
-    if (when && !hasRunOnce.current) {
-      callback();
-      hasRunOnce.current = true;
-    }
-  }, [when]);
+  useEffect(callback, [], when);
 };
+
+export const useToggle = (
+  initialValue = false,
+  defaultValue = initialValue
+) => {
+  const [value, setValue] = useState(defaultValue);
+  const toggle = () => setValue(!value);
+  return [value, toggle];
+};
+
+export const useLocalStorage = (
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,9 +1,14 @@

 const useEffectOnce = (callback, when) => {
-  const hasRunOnce = React.useRef(false);
-  React.useEffect(() => {
-    if (when && !hasRunOnce.current) {
-      callback();
-      hasRunOnce.current = true;
-    }
-  }, [when]);
+  useEffect(callback, [when]);
 };
+
+export const useWindowSize = () => {
+  const [windowSize, setWindowSize] = useState({
+    width: window.innerWidth,
+    height: window.innerHeight,
+  });
+
+  useEffectOnce(() => {
+    const handleResize = () => {
+      setWindowSize({
+        width: window.innerWidth,
```

### Accordion (task/6)

#### canonical solution

```javascript
const AccordionItem = ({ label, isCollapsed, handleClick, children }) => {
  return (
    <>
      <button className="accordion-button" onClick={handleClick}>
        {label}
      </button>
      <div
        className={`accordion-item ${isCollapsed ? 'collapsed' : 'expanded'}`}
        aria-expanded={isCollapsed}
      >
        {children}
      </div>
    </>
  );
};

const Accordion = ({ defaultIndex, onItemClick, children }) => {
  const [bindIndex, setBindIndex] = React.useState(defaultIndex);

  const changeItem = itemIndex => {
    if (typeof onItemClick === 'function') onItemClick(itemIndex);
    if (itemIndex !== bindIndex) setBindIndex(itemIndex);
  };
  const items = children.filter(item => item.type.name === 'AccordionItem');

  return (
    <>
      {items.map(({ props }) => (
        <AccordionItem
          isCollapsed={bindIndex !== props.index}
          label={props.label}
          handleClick={() => changeItem(props.index)}
          children={props.children}
        />
      ))}
    </>
  );
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,38 +1,16 @@

 const AccordionItem = ({ label, isCollapsed, handleClick, children }) => {
-  return (
-    <>
-      <button className="accordion-button" onClick={handleClick}>
-        {label}
-      </button>
-      <div
-        className={`accordion-item ${isCollapsed ? 'collapsed' : 'expanded'}`}
-        aria-expanded={isCollapsed}
-      >
-        {children}
-      </div>
-    </>
-  );
-};
+  const [collapsed, setCollapsed] = useState(isCollapsed);
 
-const Accordion = ({ defaultIndex, onItemClick, children }) => {
-  const [bindIndex, setBindIndex] = React.useState(defaultIndex);
-
-  const changeItem = itemIndex => {
-    if (typeof onItemClick === 'function') onItemClick(itemIndex);
-    if (itemIndex !== bindIndex) setBindIndex(itemIndex);
+  const toggleCollapsed = () => {
+    setCollapsed(!collapsed);
+    handleClick();
   };
-  const items = children.filter(item => item.type.name === 'AccordionItem');
 
   return (
-    <>
-      {items.map(({ props }) => (
-        <AccordionItem
-          isCollapsed={bindIndex !== props.index}
-          label={props.label}
-          handleClick={() => changeItem(props.index)}
-          children={props.children}
-        />
-      ))}
-    </>
-  );
-};
+    <div className="accordion__item">
+      <button
+        type="button"
+        className="accordion__title"
+        onClick={toggleCollapsed}
+      >
+       
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,38 +1,9 @@

 const AccordionItem = ({ label, isCollapsed, handleClick, children }) => {
+  const labelClassName = isCollapsed ? 'active' : '';
   return (
-    <>
-      <button className="accordion-button" onClick={handleClick}>
-        {label}
-      </button>
-      <div
-        className={`accordion-item ${isCollapsed ? 'collapsed' : 'expanded'}`}
-        aria-expanded={isCollapsed}
-      >
-        {children}
+    <div className="accordion__item">
+      <div className="accordion__label" onClick={handleClick}>
+        <span className={labelClassName}>{label}</span>
       </div>
-    </>
-  );
-};
-
-const Accordion = ({ defaultIndex, onItemClick, children }) => {
-  const [bindIndex, setBindIndex] = React.useState(defaultIndex);
-
-  const changeItem = itemIndex => {
-    if (typeof onItemClick === 'function') onItemClick(itemIndex);
-    if (itemIndex !== bindIndex) setBindIndex(itemIndex);
-  };
-  const items = children.filter(item => item.type.name === 'AccordionItem');
-
-  return (
-    <>
-      {items.map(({ props }) => (
-        <AccordionItem
-          isCollapsed={bindIndex !== props.index}
-          label={props.label}
-          handleClick={() => changeItem(props.index)}
-          children={props.children}
-        />
-      ))}
-    </>
-  );
-};
+      <div className="accordion__content">{children}</div>
+    </
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,38 +1,14 @@

 const AccordionItem = ({ label, isCollapsed, handleClick, children }) => {
-  return (
-    <>
-      <button className="accordion-button" onClick={handleClick}>
-        {label}
-      </button>
-      <div
-        className={`accordion-item ${isCollapsed ? 'collapsed' : 'expanded'}`}
-        aria-expanded={isCollapsed}
-      >
-        {children}
-      </div>
-    </>
-  );
-};
-
-const Accordion = ({ defaultIndex, onItemClick, children }) => {
-  const [bindIndex, setBindIndex] = React.useState(defaultIndex);
-
-  const changeItem = itemIndex => {
-    if (typeof onItemClick === 'function') onItemClick(itemIndex);
-    if (itemIndex !== bindIndex) setBindIndex(itemIndex);
-  };
-  const items = children.filter(item => item.type.name === 'AccordionItem');
+  const [isOpen, setIsOpen] = useState(isCollapsed);
 
   return (
-    <>
-      {items.map(({ props }) => (
-        <AccordionItem
-          isCollapsed={bindIndex !== props.index}
-          label={props.label}
-          handleClick={() => changeItem(props.index)}
-          children={props.children}
-        />
-      ))}
-    </>
-  );
-};
+    <div className="AccordionItem">
+      <div
+        className="AccordionItem__label"
+        onClick={() => {
+          setIsOpen(!isOpen);
+          handleClick(!isOpen);
+        }}
+      >
+        <span>{label}</span>
+        <span
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,38 +1,14 @@

 const AccordionItem = ({ label, isCollapsed, handleClick, children }) => {
-  return (
-    <>
-      <button className="accordion-button" onClick={handleClick}>
-        {label}
-      </button>
-      <div
-        className={`accordion-item ${isCollapsed ? 'collapsed' : 'expanded'}`}
-        aria-expanded={isCollapsed}
-      >
-        {children}
-      </div>
-    </>
-  );
-};
+  const [isExpanded, setIsExpanded] = useState(!isCollapsed);
 
-const Accordion = ({ defaultIndex, onItemClick, children }) => {
-  const [bindIndex, setBindIndex] = React.useState(defaultIndex);
-
-  const changeItem = itemIndex => {
-    if (typeof onItemClick === 'function') onItemClick(itemIndex);
-    if (itemIndex !== bindIndex) setBindIndex(itemIndex);
+  const onClick = () => {
+    setIsExpanded(!isExpanded);
+    handleClick(!isExpanded);
   };
-  const items = children.filter(item => item.type.name === 'AccordionItem');
 
   return (
-    <>
-      {items.map(({ props }) => (
-        <AccordionItem
-          isCollapsed={bindIndex !== props.index}
-          label={props.label}
-          handleClick={() => changeItem(props.index)}
-          children={props.children}
-        />
-      ))}
-    </>
-  );
-};
+    <div className="accordion__item">
+      <h3
+        className="accordion__title"
+        onClick={onClick}
+       
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,38 +1,13 @@

 const AccordionItem = ({ label, isCollapsed, handleClick, children }) => {
-  return (
-    <>
-      <button className="accordion-button" onClick={handleClick}>
-        {label}
-      </button>
-      <div
-        className={`accordion-item ${isCollapsed ? 'collapsed' : 'expanded'}`}
-        aria-expanded={isCollapsed}
-      >
-        {children}
-      </div>
-    </>
+  const classes = classNames(
+    "accordion-item",
+    {
+      "accordion-item--open": !isCollapsed,
+      "accordion-item--closed": isCollapsed
+    }
   );
-};
-
-const Accordion = ({ defaultIndex, onItemClick, children }) => {
-  const [bindIndex, setBindIndex] = React.useState(defaultIndex);
-
-  const changeItem = itemIndex => {
-    if (typeof onItemClick === 'function') onItemClick(itemIndex);
-    if (itemIndex !== bindIndex) setBindIndex(itemIndex);
-  };
-  const items = children.filter(item => item.type.name === 'AccordionItem');
 
   return (
-    <>
-      {items.map(({ props }) => (
-        <AccordionItem
-          isCollapsed={bindIndex !== props.index}
-          label={props.label}
-          handleClick={() => changeItem(props.index)}
-          children={props.children}
-        />
-      ))}
-    </>
-  );
-};
+    <div className={classes}>
+      <div className="accordion-item__header" onClick={handleClick}>
+        <div className="
```

### useIsomporphicEffect (task/7)

#### canonical solution

```javascript
const useIsomorphicEffect =
  typeof window !== 'undefined' ? React.useLayoutEffect : React.useEffect;
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1 +1,6 @@

-const useIsomorphicEffect =  typeof window !== 'undefined' ? React.useLayoutEffect : React.useEffect;
+const useIsomorphicEffect = typeof window !== 'undefined' ? useEffect : useLayoutEffect;
+
+export function useEventListener(eventName: string, handler: EventListenerOrEventListenerObject, element: HTMLElement | Window | Document) {
+  useIsomorphicEffect(() => {
+    const eventListener = (event: Event) => handler(event);
+
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1 +1,6 @@

-const useIsomorphicEffect =  typeof window !== 'undefined' ? React.useLayoutEffect : React.useEffect;
+const useIsomorphicEffect = typeof window !== 'undefined' ? useEffect : useLayoutEffect;
+
+function nodeIsContainedWithin(container, child) {
+  let parent = child.parentNode;
+
+  while (parent !== null) {
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1 +1,6 @@

-const useIsomorphicEffect =  typeof window !== 'undefined' ? React.useLayoutEffect : React.useEffect;
+const useIsomorphicEffect = typeof window !== 'undefined' && window.document && window.document.createElement;
+
+function useEventCallback<T extends (...args: any[]) => any>(fn: T): T {
+  const ref = useRef<T>();
+
+  useIsomorphicEffect(() => {
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1 +1,6 @@

-const useIsomorphicEffect =  typeof window !== 'undefined' ? React.useLayoutEffect : React.useEffect;
+const useIsomorphicEffect = typeof window !== 'undefined' ? React.useLayoutEffect : React.useEffect;
+
+interface Props {
+  children: React.ReactNode;
+  isOpen: boolean;
+  onClose: () => void;
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1 +1,6 @@

-const useIsomorphicEffect =  typeof window !== 'undefined' ? React.useLayoutEffect : React.useEffect;
+const useIsomorphicEffect = typeof window !== 'undefined' ? useEffect : useLayoutEffect;
+
+//
+// https://github.com/gaearon/react-hot-loader/issues/1069
+//
+
```

### useGetSet (task/8)

#### canonical solution

```javascript
const useGetSet = initialState => {
  const state = React.useRef(initialState);
  const [, update] = React.useReducer(() => ({}));

  return React.useMemo(
    () => [
      () => state.current,
      newState => {
        state.current = newState;
        update();
      },
    ],
    []
  );
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,15 +1,7 @@

 const useGetSet = initialState => {
-  const state = React.useRef(initialState);
-  const [, update] = React.useReducer(() => ({}));
+  const [state, setState] = useState(initialState);
 
-  return React.useMemo(
-    () => [
-      () => state.current,
-      newState => {
-        state.current = newState;
-        update();
-      },
-    ],
-    []
-  );
+  return [state, setState];
 };
+
+export default useGetSet;
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,15 +1,7 @@

 const useGetSet = initialState => {
-  const state = React.useRef(initialState);
-  const [, update] = React.useReducer(() => ({}));
+  const [state, setState] = useState(initialState);
 
-  return React.useMemo(
-    () => [
-      () => state.current,
-      newState => {
-        state.current = newState;
-        update();
-      },
-    ],
-    []
-  );
+  return [state, setState];
 };
+
+export default useGetSet;
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,15 +1,7 @@

 const useGetSet = initialState => {
-  const state = React.useRef(initialState);
-  const [, update] = React.useReducer(() => ({}));
+  const [state, setState] = useState(initialState);
 
-  return React.useMemo(
-    () => [
-      () => state.current,
-      newState => {
-        state.current = newState;
-        update();
-      },
-    ],
-    []
-  );
+  return [state, setState];
 };
+
+export default useGetSet;
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,15 +1,7 @@

 const useGetSet = initialState => {
-  const state = React.useRef(initialState);
-  const [, update] = React.useReducer(() => ({}));
+  const [state, setState] = useState(initialState);
 
-  return React.useMemo(
-    () => [
-      () => state.current,
-      newState => {
-        state.current = newState;
-        update();
-      },
-    ],
-    []
-  );
+  return [state, setState];
 };
+
+export default useGetSet;
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,15 +1,11 @@

 const useGetSet = initialState => {
-  const state = React.useRef(initialState);
-  const [, update] = React.useReducer(() => ({}));
+  const [data, setData] = useState(initialState);
 
-  return React.useMemo(
-    () => [
-      () => state.current,
-      newState => {
-        state.current = newState;
-        update();
-      },
-    ],
-    []
-  );
+  const getData = useCallback(() => data, [data]);
+
+  const setDataFunc = useCallback(value => setData(value), [setData]);
+
+  return [getData, setDataFunc];
 };
+
+export default useGetSet;
```

### useInterval (task/9)

#### canonical solution

```javascript
const useInterval = (callback, delay) => {
  const savedCallback = React.useRef();

  React.useEffect(() => {
    savedCallback.current = callback;
  }, [callback]);

  React.useEffect(() => {
    const tick = () => {
      savedCallback.current();
    }
    if (delay !== null) {
      let id = setInterval(tick, delay);
      return () => clearInterval(id);
    }
  }, [delay]);
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,17 +1,16 @@

 const useInterval = (callback, delay) => {
-  const savedCallback = React.useRef();
+  const savedCallback = useRef();
 
-  React.useEffect(() => {
+  // Remember the latest callback.
+  useEffect(() => {
     savedCallback.current = callback;
   }, [callback]);
 
-  React.useEffect(() => {
-    const tick = () => {
+  // Set up the interval.
+  useEffect(() => {
+    function tick() {
       savedCallback.current();
     }
     if (delay !== null) {
       let id = setInterval(tick, delay);
-      return () => clearInterval(id);
-    }
-  }, [delay]);
-};
+      return ()
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,17 +1,16 @@

 const useInterval = (callback, delay) => {
-  const savedCallback = React.useRef();
+  const savedCallback = useRef();
 
-  React.useEffect(() => {
+  // Remember the latest callback.
+  useEffect(() => {
     savedCallback.current = callback;
   }, [callback]);
 
-  React.useEffect(() => {
-    const tick = () => {
+  // Set up the interval.
+  useEffect(() => {
+    function tick() {
       savedCallback.current();
     }
     if (delay !== null) {
       let id = setInterval(tick, delay);
-      return () => clearInterval(id);
-    }
-  }, [delay]);
-};
+      return ()
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,17 +1,16 @@

 const useInterval = (callback, delay) => {
-  const savedCallback = React.useRef();
+  const savedCallback = useRef();
 
-  React.useEffect(() => {
+  // Remember the latest callback.
+  useEffect(() => {
     savedCallback.current = callback;
   }, [callback]);
 
-  React.useEffect(() => {
-    const tick = () => {
+  // Set up the interval.
+  useEffect(() => {
+    function tick() {
       savedCallback.current();
     }
     if (delay !== null) {
       let id = setInterval(tick, delay);
-      return () => clearInterval(id);
-    }
-  }, [delay]);
-};
+      return ()
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,17 +1,16 @@

 const useInterval = (callback, delay) => {
-  const savedCallback = React.useRef();
+  const savedCallback = useRef();
 
-  React.useEffect(() => {
+  // Remember the latest callback.
+  useEffect(() => {
     savedCallback.current = callback;
   }, [callback]);
 
-  React.useEffect(() => {
-    const tick = () => {
+  // Set up the interval.
+  useEffect(() => {
+    function tick() {
       savedCallback.current();
     }
     if (delay !== null) {
       let id = setInterval(tick, delay);
-      return () => clearInterval(id);
-    }
-  }, [delay]);
-};
+      return ()
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,17 +1,16 @@

 const useInterval = (callback, delay) => {
-  const savedCallback = React.useRef();
+    const savedCallback = useRef();
 
-  React.useEffect(() => {
-    savedCallback.current = callback;
-  }, [callback]);
+    // Remember the latest callback.
+    useEffect(() => {
+        savedCallback.current = callback;
+    }, [callback]);
 
-  React.useEffect(() => {
-    const tick = () => {
-      savedCallback.current();
-    }
-    if (delay !== null) {
-      let id = setInterval(tick, delay);
-      return () => clearInterval(id);
-    }
-  }, [delay]);
-};
+    // Set up the interval.
+    useEffect(() => {
+        function tick() {
+            savedCallback.current();
+        }
+        if (delay !== null) {
+            let id = setInterval(tick, delay);
+            return ()
```

### Loader (task/10)

#### canonical solution

```javascript
const Loader = ({ size }) => {
  return (
    <svg
      className="loader"
      xmlns="http://www.w3.org/2000/svg"
      width={size}
      height={size}
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <circle cx="12" cy="12" r="10" />
    </svg>
  );
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,18 +1,14 @@

 const Loader = ({ size }) => {
   return (
-    <svg
-      className="loader"
-      xmlns="http://www.w3.org/2000/svg"
-      width={size}
-      height={size}
-      viewBox="0 0 24 24"
-      fill="none"
-      stroke="currentColor"
-      strokeWidth="2"
-      strokeLinecap="round"
-      strokeLinejoin="round"
-    >
-      <circle cx="12" cy="12" r="10" />
-    </svg>
+    <div className="loader">
+      <div className="lds-ring">
+        <div></div>
+        <div></div>
+        <div></div>
+        <div></div>
+      </div>
+    </div>
   );
 };
+
+export default Loader;
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,18 +1,17 @@

 const Loader = ({ size }) => {
   return (
-    <svg
-      className="loader"
-      xmlns="http://www.w3.org/2000/svg"
-      width={size}
-      height={size}
-      viewBox="0 0 24 24"
-      fill="none"
-      stroke="currentColor"
-      strokeWidth="2"
-      strokeLinecap="round"
-      strokeLinejoin="round"
-    >
-      <circle cx="12" cy="12" r="10" />
-    </svg>
+    <div>
+      <img src={loadingIcon} alt="Loading Icon" className={`loader-${size}`} />
+    </div>
   );
 };
+
+Loader.propTypes = {
+  size: PropTypes.string
+};
+
+Loader.defaultProps = {
+  size: 'medium'
+};
+
+export default Loader;
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,18 +1,12 @@

 const Loader = ({ size }) => {
   return (
-    <svg
-      className="loader"
-      xmlns="http://www.w3.org/2000/svg"
-      width={size}
-      height={size}
-      viewBox="0 0 24 24"
-      fill="none"
-      stroke="currentColor"
-      strokeWidth="2"
-      strokeLinecap="round"
-      strokeLinejoin="round"
-    >
-      <circle cx="12" cy="12" r="10" />
-    </svg>
-  );
-};
+    <div className="loadingio-spinner-double-ring-r64jb2mr8s">
+      <div className="ldio-6tp9m3zq3l">
+        <div></div>
+        <div></div>
+        <div>
+          <div></div>
+        </div>
+        <div>
+          <div></div>
+        </div>
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,18 +1,11 @@

 const Loader = ({ size }) => {
   return (
     <svg
-      className="loader"
-      xmlns="http://www.w3.org/2000/svg"
       width={size}
       height={size}
-      viewBox="0 0 24 24"
-      fill="none"
-      stroke="currentColor"
-      strokeWidth="2"
-      strokeLinecap="round"
-      strokeLinejoin="round"
+      viewBox="0 0 38 38"
+      xmlns="http://www.w3.org/2000/svg"
     >
-      <circle cx="12" cy="12" r="10" />
-    </svg>
-  );
-};
+      <g stroke="none" strokeWidth="1" fill="none" fillRule="evenodd">
+        <g transform="translate(1.000000, 1.000000)" fill="#000000">
+         
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,18 +1,17 @@

 const Loader = ({ size }) => {
   return (
-    <svg
-      className="loader"
-      xmlns="http://www.w3.org/2000/svg"
-      width={size}
-      height={size}
-      viewBox="0 0 24 24"
-      fill="none"
-      stroke="currentColor"
-      strokeWidth="2"
-      strokeLinecap="round"
-      strokeLinejoin="round"
-    >
-      <circle cx="12" cy="12" r="10" />
-    </svg>
+    <LoaderContainer>
+      <LoaderIcon size={size} />
+    </LoaderContainer>
   );
 };
+
+Loader.propTypes = {
+  size: PropTypes.number,
+};
+
+Loader.defaultProps = {
+  size: 50,
+};
+
+export default Loader;
```

### Modal (task/11)

#### canonical solution

```javascript
const Modal = ({ isVisible = false, title, content, footer, onClose }) => {
  const keydownHandler = ({ key }) => {
    switch (key) {
      case 'Escape':
        onClose();
        break;
      default:
    }
  };

  React.useEffect(() => {
    document.addEventListener('keydown', keydownHandler);
    return () => document.removeEventListener('keydown', keydownHandler);
  });

  return !isVisible ? null : (
    <div className="modal" onClick={onClose}>
      <div className="modal-dialog" onClick={e => e.stopPropagation()}>
        <div className="modal-header">
          <h3 className="modal-title">{title}</h3>
          <span className="modal-close" onClick={onClose}>
            &times;
          </span>
        </div>
        <div className="modal-body">
          <div className="modal-content">{content}</div>
        </div>
        {footer && <div className="modal-footer">{footer}</div>}
      </div>
    </div>
  );
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,32 +1,14 @@

 const Modal = ({ isVisible = false, title, content, footer, onClose }) => {
-  const keydownHandler = ({ key }) => {
-    switch (key) {
-      case 'Escape':
-        onClose();
-        break;
-      default:
-    }
-  };
+  const handleOnClose = () => {
+    onClose()
+  }
 
-  React.useEffect(() => {
-    document.addEventListener('keydown', keydownHandler);
-    return () => document.removeEventListener('keydown', keydownHandler);
-  });
-
-  return !isVisible ? null : (
-    <div className="modal" onClick={onClose}>
-      <div className="modal-dialog" onClick={e => e.stopPropagation()}>
-        <div className="modal-header">
-          <h3 className="modal-title">{title}</h3>
-          <span className="modal-close" onClick={onClose}>
-            &times;
-          </span>
-        </div>
-        <div className="modal-body">
-          <div className="modal-content">{content}</div>
-        </div>
-        {footer && <div className="modal-footer">{footer}</div>}
-      </div>
-    </div>
-  );
-};
+  return (
+    <ModalStyle isVisible={isVisible}>
+      <Container>
+        <Header>
+          <Title>{title}</Title>
+          <Close onClick={handleOnClose}>x</Close>
+        </Header>
+        <Content>{content}</Content>
+        <Footer>{footer
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,32 +1,13 @@

 const Modal = ({ isVisible = false, title, content, footer, onClose }) => {
-  const keydownHandler = ({ key }) => {
-    switch (key) {
-      case 'Escape':
-        onClose();
-        break;
-      default:
+  const handleClick = (event) => {
+    const target = event.target;
+    if (target === event.currentTarget) {
+      onClose();
     }
   };
 
-  React.useEffect(() => {
-    document.addEventListener('keydown', keydownHandler);
-    return () => document.removeEventListener('keydown', keydownHandler);
-  });
-
-  return !isVisible ? null : (
-    <div className="modal" onClick={onClose}>
-      <div className="modal-dialog" onClick={e => e.stopPropagation()}>
+  return (
+    <ModalContainer isVisible={isVisible} onClick={handleClick}>
+      <ModalInner>
         <div className="modal-header">
-          <h3 className="modal-title">{title}</h3>
-          <span className="modal-close" onClick={onClose}>
-            &times;
-          </span>
-        </div>
-        <div className="modal-body">
-          <div className="modal-content">{content}</div>
-        </div>
-        {footer && <div className="modal-footer">{footer}</div>}
-      </div>
-    </div>
-  );
-};
+          <span className="modal-title
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,32 +1,11 @@

 const Modal = ({ isVisible = false, title, content, footer, onClose }) => {
-  const keydownHandler = ({ key }) => {
-    switch (key) {
-      case 'Escape':
-        onClose();
-        break;
-      default:
-    }
-  };
+  const [isVisibleClassName, setIsVisibleClassName] = useState(
+    isVisible ? 'modal--visible' : ''
+  );
 
-  React.useEffect(() => {
-    document.addEventListener('keydown', keydownHandler);
-    return () => document.removeEventListener('keydown', keydownHandler);
-  });
+  useEffect(() => {
+    setIsVisibleClassName(isVisible ? 'modal--visible' : '');
+  }, [isVisible]);
 
-  return !isVisible ? null : (
-    <div className="modal" onClick={onClose}>
-      <div className="modal-dialog" onClick={e => e.stopPropagation()}>
-        <div className="modal-header">
-          <h3 className="modal-title">{title}</h3>
-          <span className="modal-close" onClick={onClose}>
-            &times;
-          </span>
-        </div>
-        <div className="modal-body">
-          <div className="modal-content">{content}</div>
-        </div>
-        {footer && <div className="modal-footer">{footer}</div>}
-      </div>
-    </div>
-  );
-};
+  return (
+    <div className={`modal ${isVisibleClassName}`}
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,32 +1,10 @@

 const Modal = ({ isVisible = false, title, content, footer, onClose }) => {
-  const keydownHandler = ({ key }) => {
-    switch (key) {
-      case 'Escape':
-        onClose();
-        break;
-      default:
-    }
-  };
-
-  React.useEffect(() => {
-    document.addEventListener('keydown', keydownHandler);
-    return () => document.removeEventListener('keydown', keydownHandler);
-  });
-
-  return !isVisible ? null : (
-    <div className="modal" onClick={onClose}>
-      <div className="modal-dialog" onClick={e => e.stopPropagation()}>
-        <div className="modal-header">
-          <h3 className="modal-title">{title}</h3>
-          <span className="modal-close" onClick={onClose}>
-            &times;
-          </span>
-        </div>
-        <div className="modal-body">
-          <div className="modal-content">{content}</div>
-        </div>
-        {footer && <div className="modal-footer">{footer}</div>}
-      </div>
-    </div>
-  );
-};
+  const classes = useStyles();
+  return (
+    <div className={classes.root}>
+      <ModalDialog isVisible={isVisible} onClose={onClose}>
+        <div className={classes.paper}>
+          <div className={classes.header}>
+            <Typography className={classes.title}>{title}</Typography>
+            <IconButton
+              aria
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,32 +1,9 @@

 const Modal = ({ isVisible = false, title, content, footer, onClose }) => {
-  const keydownHandler = ({ key }) => {
-    switch (key) {
-      case 'Escape':
-        onClose();
-        break;
-      default:
-    }
-  };
+  const isContentEmpty = content === null || content === undefined;
+  const hasTitle = title !== null && title !== undefined;
+  const hasFooter = footer !== null && footer !== undefined;
 
-  React.useEffect(() => {
-    document.addEventListener('keydown', keydownHandler);
-    return () => document.removeEventListener('keydown', keydownHandler);
-  });
-
-  return !isVisible ? null : (
-    <div className="modal" onClick={onClose}>
-      <div className="modal-dialog" onClick={e => e.stopPropagation()}>
-        <div className="modal-header">
-          <h3 className="modal-title">{title}</h3>
-          <span className="modal-close" onClick={onClose}>
-            &times;
-          </span>
-        </div>
-        <div className="modal-body">
-          <div className="modal-content">{content}</div>
-        </div>
-        {footer && <div className="modal-footer">{footer}</div>}
-      </div>
-    </div>
-  );
-};
+  return (
+    <div className={cx('Modal', { 'Modal--visible': isVisible })}>
+      <div className="Modal__container">
+        <div className="
```

### useIntersectionObserver (task/12)

#### canonical solution

```javascript
const useIntersectionObserver = (ref, options) => {
  const [isIntersecting, setIsIntersecting] = React.useState(false);

  React.useEffect(() => {
    const observer = new IntersectionObserver(([entry]) => {
      setIsIntersecting(entry.isIntersecting);
    }, options);

    if (ref.current) {
      observer.observe(ref.current);
    }

    return () => {
      observer.unobserve(ref.current);
    };
  }, []);

  return isIntersecting;
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,19 +1,13 @@

 const useIntersectionObserver = (ref, options) => {
-  const [isIntersecting, setIsIntersecting] = React.useState(false);
+  const [entry, setEntry] = useState(null);
+  const observer = useRef(null);
 
-  React.useEffect(() => {
-    const observer = new IntersectionObserver(([entry]) => {
-      setIsIntersecting(entry.isIntersecting);
+  useEffect(() => {
+    observer.current = new IntersectionObserver(entries => {
+      setEntry(entries[0]);
     }, options);
-
     if (ref.current) {
-      observer.observe(ref.current);
+      observer.current.observe(ref.current);
     }
-
     return () => {
-      observer.unobserve(ref.current);
-    };
-  }, []);
-
-  return isIntersecting;
-};
+      observer
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,19 +1,12 @@

 const useIntersectionObserver = (ref, options) => {
-  const [isIntersecting, setIsIntersecting] = React.useState(false);
+  const [isIntersecting, setIsIntersecting] = useState(false);
 
-  React.useEffect(() => {
-    const observer = new IntersectionObserver(([entry]) => {
-      setIsIntersecting(entry.isIntersecting);
+  useEffect(() => {
+    const observer = new IntersectionObserver(entries => {
+      const { isIntersecting } = entries[0];
+      setIsIntersecting(isIntersecting);
     }, options);
 
     if (ref.current) {
       observer.observe(ref.current);
-    }
-
-    return () => {
-      observer.unobserve(ref.current);
-    };
-  }, []);
-
-  return isIntersecting;
-};
+   
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,19 +1,14 @@

 const useIntersectionObserver = (ref, options) => {
-  const [isIntersecting, setIsIntersecting] = React.useState(false);
+  const [entry, setEntry] = useState();
+  const [entries, setEntries] = useState();
+  const [{ isIntersecting }, setIsIntersecting] = useState();
 
-  React.useEffect(() => {
-    const observer = new IntersectionObserver(([entry]) => {
-      setIsIntersecting(entry.isIntersecting);
-    }, options);
+  useEffect(() => {
+    const io = new IntersectionObserver(
+      ([entry]) => {
+        setEntry(entry);
+      },
+      options
+    );
 
     if (ref.current) {
-      observer.observe(ref.current);
-    }
-
-    return () => {
-      observer.unobserve(ref.current);
-    };
-  }, []);
-
-  return isIntersecting;
-};
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,19 +1,14 @@

 const useIntersectionObserver = (ref, options) => {
-  const [isIntersecting, setIsIntersecting] = React.useState(false);
+  const [entry, setEntry] = useState(null);
+  const [isIntersecting, setIsIntersecting] = useState(false);
 
-  React.useEffect(() => {
-    const observer = new IntersectionObserver(([entry]) => {
-      setIsIntersecting(entry.isIntersecting);
-    }, options);
+  useEffect(() => {
+    const observer = new IntersectionObserver(
+      ([entry]) => {
+        setEntry(entry);
+        setIsIntersecting(entry.isIntersecting);
+      },
+      options
+    );
 
-    if (ref.current) {
-      observer.observe(ref.current);
-    }
-
-    return () => {
-      observer.unobserve(ref.current);
-    };
-  }, []);
-
-  return isIntersecting;
-};
+    observer.obser
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,19 +1,13 @@

 const useIntersectionObserver = (ref, options) => {
-  const [isIntersecting, setIsIntersecting] = React.useState(false);
+  const [entry, setEntry] = useState(null);
+  const [node, setNode] = useState(null);
 
-  React.useEffect(() => {
-    const observer = new IntersectionObserver(([entry]) => {
-      setIsIntersecting(entry.isIntersecting);
+  useEffect(() => {
+    const observer = new IntersectionObserver(entries => {
+      if (entries[0].isIntersecting) {
+        setEntry(entries[0]);
+        setNode(ref.current);
+      }
     }, options);
 
-    if (ref.current) {
-      observer.observe(ref.current);
-    }
-
-    return () => {
-      observer.unobserve(ref.current);
-    };
-  }, []);
-
-  return isIntersecting;
-};
+    if (
```

### Slider (task/13)

#### canonical solution

```javascript
const Slider = ({ 
  min = 0,
  max = 100,
  defaultValue,
  onValueChange,
  ...rest
}) => {
  return (
    <input
      type="range"
      min={min}
      max={max}
      defaultValue={defaultValue}
      onChange={({ target: { value } }) => onValueChange(value)}
      {...rest}
    />
  );
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,17 +1,14 @@

-const Slider = ({   min = 0,
-  max = 100,
-  defaultValue,
-  onValueChange,
-  ...rest
-}) => {
+const Slider = ({ value, onChange }) => {
   return (
-    <input
-      type="range"
-      min={min}
-      max={max}
-      defaultValue={defaultValue}
-      onChange={({ target: { value } }) => onValueChange(value)}
-      {...rest}
-    />
+    <div className="slider">
+      <SliderTrack>
+        <SliderThumb value={value} onChange={onChange} />
+      </SliderTrack>
+    </div>
   );
 };
+
+Slider.propTypes = {
+  value: PropTypes.number.isRequired,
+  onChange: PropTypes.func.isRequired,
+};
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,17 +1,14 @@

-const Slider = ({   min = 0,
-  max = 100,
-  defaultValue,
-  onValueChange,
-  ...rest
-}) => {
-  return (
-    <input
-      type="range"
-      min={min}
-      max={max}
-      defaultValue={defaultValue}
-      onChange={({ target: { value } }) => onValueChange(value)}
-      {...rest}
-    />
-  );
-};
+const Slider = ({ x, y, size, onClick, onHover, isSelected, label, value, suffix, onChange }) => {
+  const handleClick = (event) => {
+    if (onClick) {
+      onClick(event);
+    }
+  };
+
+  const handleMouseOver = (event) => {
+    if (onHover) {
+      onHover(event);
+    }
+  };
+
+  const handleMouse
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,17 +1,14 @@

-const Slider = ({   min = 0,
-  max = 100,
-  defaultValue,
-  onValueChange,
-  ...rest
-}) => {
+const Slider = ({ value, min, max, step, onChange }) => {
+  const [localValue, setLocalValue] = useState(value);
+
+  useEffect(() => {
+    setLocalValue(value);
+  }, [value]);
+
+  const handleChange = (event, newValue) => {
+    setLocalValue(newValue);
+    onChange(newValue);
+  };
+
   return (
-    <input
-      type="range"
-      min={min}
-      max={max}
-      defaultValue={defaultValue}
-      onChange={({ target: { value } }) => onValueChange(value)}
-      {...rest}
-    />
-  );
-};
+    <Grid container spacing={2} align
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,17 +1,13 @@

-const Slider = ({   min = 0,
-  max = 100,
-  defaultValue,
-  onValueChange,
-  ...rest
-}) => {
+const Slider = ({ getPosition, id, label, value, options, setValue }) => {
+  const handleChange = (event, newValue) => {
+    setValue(newValue);
+  };
+
   return (
-    <input
-      type="range"
-      min={min}
-      max={max}
-      defaultValue={defaultValue}
-      onChange={({ target: { value } }) => onValueChange(value)}
-      {...rest}
-    />
-  );
-};
+    <Card className="slider-card">
+      <Typography variant="h5" component="h2">
+        {label}
+      </Typography>
+      <Slider
+        min={options.min}
+        max={
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,17 +1,17 @@

-const Slider = ({   min = 0,
-  max = 100,
-  defaultValue,
-  onValueChange,
-  ...rest
-}) => {
+const Slider = ({ max, onChange, value }) => {
+  const handleChange = (event, newValue) => {
+    onChange(newValue);
+  };
+
   return (
-    <input
-      type="range"
-      min={min}
-      max={max}
-      defaultValue={defaultValue}
-      onChange={({ target: { value } }) => onValueChange(value)}
-      {...rest}
-    />
-  );
-};
+    <div>
+      <Slider
+        min={0}
+        max={max}
+        value={value}
+        onChange={handleChange}
+        valueLabelDisplay="auto"
+        marks
+        step={1}
+      />
+    </div>
```

### useToggler (task/14)

#### canonical solution

```javascript
const useToggler = initialState => {
  const [value, setValue] = React.useState(initialState);

  const toggleValue = React.useCallback(() => setValue(prev => !prev), []);

  return [value, toggleValue];
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,7 +1,12 @@

 const useToggler = initialState => {
-  const [value, setValue] = React.useState(initialState);
+  const [isToggled, setToggled] = useState(initialState);
 
-  const toggleValue = React.useCallback(() => setValue(prev => !prev), []);
+  const handleToggle = () => {
+    setToggled(prevState => !prevState);
+  };
 
-  return [value, toggleValue];
+  return {
+    isToggled,
+    handleToggle
+  };
 };
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,7 +1,9 @@

 const useToggler = initialState => {
-  const [value, setValue] = React.useState(initialState);
+	const [isToggled, setToggled] = useState(initialState);
 
-  const toggleValue = React.useCallback(() => setValue(prev => !prev), []);
+	const toggle = () => setToggled(!isToggled);
 
-  return [value, toggleValue];
+	return [isToggled, toggle];
 };
+
+export default useToggler;
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,7 +1,9 @@

 const useToggler = initialState => {
-  const [value, setValue] = React.useState(initialState);
+  const [isOpen, setIsOpen] = useState(initialState);
 
-  const toggleValue = React.useCallback(() => setValue(prev => !prev), []);
+  const toggle = () => setIsOpen(!isOpen);
 
-  return [value, toggleValue];
+  return { isOpen, toggle };
 };
+
+export default useToggler;
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,7 +1,11 @@

 const useToggler = initialState => {
-  const [value, setValue] = React.useState(initialState);
+  const [state, setState] = useState(initialState);
 
-  const toggleValue = React.useCallback(() => setValue(prev => !prev), []);
+  const toggler = useCallback(() => {
+    setState(currentState => !currentState);
+  }, []);
 
-  return [value, toggleValue];
+  return [state, toggler];
 };
+
+export default useToggler;
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,7 +1,9 @@

 const useToggler = initialState => {
-  const [value, setValue] = React.useState(initialState);
+  const [isToggled, setToggled] = useState(initialState);
 
-  const toggleValue = React.useCallback(() => setValue(prev => !prev), []);
+  const toggle = () => setToggled(!isToggled);
 
-  return [value, toggleValue];
+  return [isToggled, toggle];
 };
+
+export default useToggler;
```

### useHover (task/15)

#### canonical solution

```javascript
const useHover = () => {
  const [isHovering, setIsHovering] = React.useState(false);

  const handleMouseOver = React.useCallback(() => setIsHovering(true), []);
  const handleMouseOut = React.useCallback(() => setIsHovering(false), []);

  const nodeRef = React.useRef();

  const callbackRef = React.useCallback(
    node => {
      if (nodeRef.current) {
        nodeRef.current.removeEventListener('mouseover', handleMouseOver);
        nodeRef.current.removeEventListener('mouseout', handleMouseOut);
      }

      nodeRef.current = node;

      if (nodeRef.current) {
        nodeRef.current.addEventListener('mouseover', handleMouseOver);
        nodeRef.current.addEventListener('mouseout', handleMouseOut);
      }
    },
    [handleMouseOver, handleMouseOut]
  );

  return [callbackRef, isHovering];
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,27 +1,10 @@

 const useHover = () => {
-  const [isHovering, setIsHovering] = React.useState(false);
+  const [hover, setHover] = useState(false);
+  const onMouseOver = () => setHover(true);
+  const onMouseOut = () => setHover(false);
+  return { hover, onMouseOver, onMouseOut };
+};
 
-  const handleMouseOver = React.useCallback(() => setIsHovering(true), []);
-  const handleMouseOut = React.useCallback(() => setIsHovering(false), []);
-
-  const nodeRef = React.useRef();
-
-  const callbackRef = React.useCallback(
-    node => {
-      if (nodeRef.current) {
-        nodeRef.current.removeEventListener('mouseover', handleMouseOver);
-        nodeRef.current.removeEventListener('mouseout', handleMouseOut);
-      }
-
-      nodeRef.current = node;
-
-      if (nodeRef.current) {
-        nodeRef.current.addEventListener('mouseover', handleMouseOver);
-        nodeRef.current.addEventListener('mouseout', handleMouseOut);
-      }
-    },
-    [handleMouseOver, handleMouseOut]
-  );
-
-  return [callbackRef, isHovering];
-};
+const useAnimation = (duration = 1000) => {
+  const [isAnimated, setAnimated] = useState(false);
+  const animationStyles
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,27 +1,15 @@

 const useHover = () => {
-  const [isHovering, setIsHovering] = React.useState(false);
+  const [hover, setHover] = useState(false);
+  const ref = useRef(null);
 
-  const handleMouseOver = React.useCallback(() => setIsHovering(true), []);
-  const handleMouseOut = React.useCallback(() => setIsHovering(false), []);
+  useEffect(() => {
+    function handleMouseOver() {
+      setHover(true);
+    }
 
-  const nodeRef = React.useRef();
+    function handleMouseOut() {
+      setHover(false);
+    }
 
-  const callbackRef = React.useCallback(
-    node => {
-      if (nodeRef.current) {
-        nodeRef.current.removeEventListener('mouseover', handleMouseOver);
-        nodeRef.current.removeEventListener('mouseout', handleMouseOut);
-      }
-
-      nodeRef.current = node;
-
-      if (nodeRef.current) {
-        nodeRef.current.addEventListener('mouseover', handleMouseOver);
-        nodeRef.current.addEventListener('mouseout', handleMouseOut);
-      }
-    },
-    [handleMouseOver, handleMouseOut]
-  );
-
-  return [callbackRef, isHovering];
-};
+    ref.current.addEventListener('mouseover', handleMouseOver);
+    ref.current.addEventListener('
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,27 +1,14 @@

 const useHover = () => {
-  const [isHovering, setIsHovering] = React.useState(false);
+  const [hovered, setHovered] = useState(false);
 
-  const handleMouseOver = React.useCallback(() => setIsHovering(true), []);
-  const handleMouseOut = React.useCallback(() => setIsHovering(false), []);
+  const onMouseEnter = () => setHovered(true);
+  const onMouseLeave = () => setHovered(false);
 
-  const nodeRef = React.useRef();
+  return {
+    hovered,
+    onMouseEnter,
+    onMouseLeave,
+  };
+};
 
-  const callbackRef = React.useCallback(
-    node => {
-      if (nodeRef.current) {
-        nodeRef.current.removeEventListener('mouseover', handleMouseOver);
-        nodeRef.current.removeEventListener('mouseout', handleMouseOut);
-      }
-
-      nodeRef.current = node;
-
-      if (nodeRef.current) {
-        nodeRef.current.addEventListener('mouseover', handleMouseOver);
-        nodeRef.current.addEventListener('mouseout', handleMouseOut);
-      }
-    },
-    [handleMouseOver, handleMouseOut]
-  );
-
-  return [callbackRef, isHovering];
-};
+export default useHover;
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,27 +1,7 @@

 const useHover = () => {
-  const [isHovering, setIsHovering] = React.useState(false);
+  const [hovered, setHovered] = useState(false);
+  const toggleHover = () => setHovered(!hovered);
+  return { hovered, toggleHover };
+};
 
-  const handleMouseOver = React.useCallback(() => setIsHovering(true), []);
-  const handleMouseOut = React.useCallback(() => setIsHovering(false), []);
-
-  const nodeRef = React.useRef();
-
-  const callbackRef = React.useCallback(
-    node => {
-      if (nodeRef.current) {
-        nodeRef.current.removeEventListener('mouseover', handleMouseOver);
-        nodeRef.current.removeEventListener('mouseout', handleMouseOut);
-      }
-
-      nodeRef.current = node;
-
-      if (nodeRef.current) {
-        nodeRef.current.addEventListener('mouseover', handleMouseOver);
-        nodeRef.current.addEventListener('mouseout', handleMouseOut);
-      }
-    },
-    [handleMouseOver, handleMouseOut]
-  );
-
-  return [callbackRef, isHovering];
-};
+export default useHover;
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,27 +1,15 @@

 const useHover = () => {
-  const [isHovering, setIsHovering] = React.useState(false);
+  const [isHovering, setIsHovering] = useState(false);
+  const ref = useRef(null);
 
-  const handleMouseOver = React.useCallback(() => setIsHovering(true), []);
-  const handleMouseOut = React.useCallback(() => setIsHovering(false), []);
+  const handleMouseOver = () => {
+    setIsHovering(true);
+  };
 
-  const nodeRef = React.useRef();
+  const handleMouseOut = () => {
+    setIsHovering(false);
+  };
 
-  const callbackRef = React.useCallback(
-    node => {
-      if (nodeRef.current) {
-        nodeRef.current.removeEventListener('mouseover', handleMouseOver);
-        nodeRef.current.removeEventListener('mouseout', handleMouseOut);
-      }
-
-      nodeRef.current = node;
-
-      if (nodeRef.current) {
-        nodeRef.current.addEventListener('mouseover', handleMouseOver);
-        nodeRef.current.addEventListener('mouseout', handleMouseOut);
-      }
-    },
-    [handleMouseOver, handleMouseOut]
-  );
-
-  return [callbackRef, isHovering];
-};
+  useEffect(() => {
+    const node = ref.current;
+    if (node
```

### usePrevious (task/16)

#### canonical solution

```javascript
const usePrevious = value => {
  const ref = React.useRef();
  React.useEffect(() => {
    ref.current = value;
  });
  return ref.current;
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,7 +1,12 @@

 const usePrevious = value => {
-  const ref = React.useRef();
-  React.useEffect(() => {
+  const ref = useRef();
+  useEffect(() => {
     ref.current = value;
   });
   return ref.current;
 };
+
+export const useLocalStorage = (
+  key,
+  initialValue,
+  type = 'value',
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,7 +1,12 @@

 const usePrevious = value => {
-  const ref = React.useRef();
-  React.useEffect(() => {
+  const ref = useRef();
+  useEffect(() => {
     ref.current = value;
   });
   return ref.current;
 };
+
+const App: React.FC = () => {
+  const state = useGlobalState();
+  const prevState = usePrevious(state);
+  const updateContent = useCallback(
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,7 +1,12 @@

 const usePrevious = value => {
-  const ref = React.useRef();
-  React.useEffect(() => {
+  const ref = useRef();
+  useEffect(() => {
     ref.current = value;
   });
   return ref.current;
 };
+
+export const usePortal = name => {
+  const [isOpen, setIsOpen] = useState(false);
+  const previousName = usePrevious(name);
+  const [state, dispatch] = useReducer(reducer, null);
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,7 +1,9 @@

 const usePrevious = value => {
-  const ref = React.useRef();
-  React.useEffect(() => {
+  const ref = useRef();
+  useEffect(() => {
     ref.current = value;
   });
   return ref.current;
 };
+
+export default usePrevious;
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,7 +1,12 @@

 const usePrevious = value => {
-  const ref = React.useRef();
-  React.useEffect(() => {
-    ref.current = value;
-  });
-  return ref.current;
+    const ref = useRef();
+    useEffect(() => {
+        ref.current = value;
+    });
+    return ref.current;
 };
+
+const useSearchState = (initialValue) => {
+    const [search, setSearch] = useState(initialValue);
+    const prevSearch = usePrevious(search);
+
```

### useMediaQuery (task/17)

#### canonical solution

```javascript
const useMediaQuery = (query, whenTrue, whenFalse) => {
  if (typeof window === 'undefined' || typeof window.matchMedia === 'undefined')
    return whenFalse;

  const mediaQuery = window.matchMedia(query);
  const [match, setMatch] = React.useState(!!mediaQuery.matches);

  React.useEffect(() => {
    const handler = () => setMatch(!!mediaQuery.matches);
    mediaQuery.addListener(handler);
    return () => mediaQuery.removeListener(handler);
  }, []);

  return match ? whenTrue : whenFalse;
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,15 +1,13 @@

 const useMediaQuery = (query, whenTrue, whenFalse) => {
-  if (typeof window === 'undefined' || typeof window.matchMedia === 'undefined')
-    return whenFalse;
+    const mql = window.matchMedia(query);
+    let hasMatch = mql.matches;
+    if (hasMatch) {
+        return whenTrue;
+    } else {
+        return whenFalse;
+    }
+};
 
-  const mediaQuery = window.matchMedia(query);
-  const [match, setMatch] = React.useState(!!mediaQuery.matches);
-
-  React.useEffect(() => {
-    const handler = () => setMatch(!!mediaQuery.matches);
-    mediaQuery.addListener(handler);
-    return () => mediaQuery.removeListener(handler);
-  }, []);
-
-  return match ? whenTrue : whenFalse;
-};
+export const useScreenWidth = () => {
+    const [width, setWidth] = useState(useMediaQuery('(min-width: 500px)', 500, 320));
+    use
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,15 +1,15 @@

 const useMediaQuery = (query, whenTrue, whenFalse) => {
-  if (typeof window === 'undefined' || typeof window.matchMedia === 'undefined')
-    return whenFalse;
+    const mediaQueryList = window.matchMedia(query);
+    let currentValue = null;
+    const onQueryChange = (event) => {
+        if (event.matches) {
+            currentValue = whenTrue;
+        } else {
+            currentValue = whenFalse;
+        }
+    };
+    onQueryChange(mediaQueryList);
+    return [currentValue, onQueryChange];
+};
 
-  const mediaQuery = window.matchMedia(query);
-  const [match, setMatch] = React.useState(!!mediaQuery.matches);
-
-  React.useEffect(() => {
-    const handler = () => setMatch(!!mediaQuery.matches);
-    mediaQuery.addListener(handler);
-    return () => mediaQuery.removeListener(handler);
-  }, []);
-
-  return match ? whenTrue : whenFalse;
-};
+export default use
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,15 +1,12 @@

 const useMediaQuery = (query, whenTrue, whenFalse) => {
-  if (typeof window === 'undefined' || typeof window.matchMedia === 'undefined')
-    return whenFalse;
+  const [matches, setMatches] = useState(
+    window.matchMedia(query).matches
+  );
 
-  const mediaQuery = window.matchMedia(query);
-  const [match, setMatch] = React.useState(!!mediaQuery.matches);
+  useEffect(() => {
+    const handler = e => setMatches(e.matches);
+    window.matchMedia(query).addListener(handler);
+    return () => window.matchMedia(query).removeListener(handler);
+  }, [query]);
 
-  React.useEffect(() => {
-    const handler = () => setMatch(!!mediaQuery.matches);
-    mediaQuery.addListener(handler);
-    return () => mediaQuery.removeListener(handler);
-  }, []);
-
-  return match ? whenTrue : whenFalse;
-};
+  return matches ? whenTrue : when
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,15 +1,9 @@

 const useMediaQuery = (query, whenTrue, whenFalse) => {
-  if (typeof window === 'undefined' || typeof window.matchMedia === 'undefined')
-    return whenFalse;
+  return useContext(MediaQueryContext) === query ? whenTrue : whenFalse;
+};
 
-  const mediaQuery = window.matchMedia(query);
-  const [match, setMatch] = React.useState(!!mediaQuery.matches);
+const useMediaQueryWithContext = (query, whenTrue, whenFalse) => {
+  return useContext(MediaQueryContext) === query ? whenTrue : whenFalse;
+};
 
-  React.useEffect(() => {
-    const handler = () => setMatch(!!mediaQuery.matches);
-    mediaQuery.addListener(handler);
-    return () => mediaQuery.removeListener(handler);
-  }, []);
-
-  return match ? whenTrue : whenFalse;
-};
+export { useMediaQuery, useMediaQueryWithContext };
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,15 +1,10 @@

 const useMediaQuery = (query, whenTrue, whenFalse) => {
-  if (typeof window === 'undefined' || typeof window.matchMedia === 'undefined')
-    return whenFalse;
+    const mediaQuery = window.matchMedia(query);
+    if (mediaQuery.matches) {
+        return whenTrue;
+    } else {
+        return whenFalse;
+    }
+};
 
-  const mediaQuery = window.matchMedia(query);
-  const [match, setMatch] = React.useState(!!mediaQuery.matches);
-
-  React.useEffect(() => {
-    const handler = () => setMatch(!!mediaQuery.matches);
-    mediaQuery.addListener(handler);
-    return () => mediaQuery.removeListener(handler);
-  }, []);
-
-  return match ? whenTrue : whenFalse;
-};
+export default useMediaQuery;
```

### useDefault (task/18)

#### canonical solution

```javascript
const useDefault = (defaultState, initialState) => {
  const [value, setValue] = React.useState(initialState);
  const isValueEmpty = value === undefined || value === null;
  return [isValueEmpty ? defaultState : value, setValue];
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,5 +1,9 @@

 const useDefault = (defaultState, initialState) => {
-  const [value, setValue] = React.useState(initialState);
-  const isValueEmpty = value === undefined || value === null;
-  return [isValueEmpty ? defaultState : value, setValue];
+  const [state, setState] = useState(() =>
+    initialState === undefined ? defaultState : initialState
+  );
+
+  return [state, setState];
 };
+
+export default useDefault;
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,5 +1,10 @@

 const useDefault = (defaultState, initialState) => {
-  const [value, setValue] = React.useState(initialState);
-  const isValueEmpty = value === undefined || value === null;
-  return [isValueEmpty ? defaultState : value, setValue];
+    const initialStateIsUndefined = typeof initialState === 'undefined';
+    const isInitialStateDefault = initialState === defaultState;
+    if (initialStateIsUndefined || isInitialStateDefault) {
+        return defaultState;
+    }
+    return initialState;
 };
+const createReducer = (reducers, defaultState) => (state, action) => {
+    if (typeof reducers === 'function')
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,5 +1,9 @@

 const useDefault = (defaultState, initialState) => {
-  const [value, setValue] = React.useState(initialState);
-  const isValueEmpty = value === undefined || value === null;
-  return [isValueEmpty ? defaultState : value, setValue];
+    const [state, setState] = useState(() =>
+        initialState === undefined ? defaultState : initialState
+    );
+
+    return [state, setState];
 };
+
+export default useDefault;
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,5 +1,10 @@

 const useDefault = (defaultState, initialState) => {
-  const [value, setValue] = React.useState(initialState);
-  const isValueEmpty = value === undefined || value === null;
-  return [isValueEmpty ? defaultState : value, setValue];
+  return (
+    initialState === undefined ? defaultState : initialState
+  );
 };
+
+const useCallbackCondition = (callback, condition) => {
+  return useMemo(() => condition ? callback : null, [condition]);
+};
+
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,5 +1,10 @@

 const useDefault = (defaultState, initialState) => {
-  const [value, setValue] = React.useState(initialState);
-  const isValueEmpty = value === undefined || value === null;
-  return [isValueEmpty ? defaultState : value, setValue];
+  return Object.keys(defaultState).reduce((acc, key) => {
+    if (initialState[key] === undefined) {
+      acc[key] = defaultState[key];
+    } else {
+      acc[key] = initialState[key];
+    }
+    return acc;
+  }, {});
 };
```

### TagInput (task/19)

#### canonical solution

```javascript
const TagInput = ({ tags }) => {
  const [tagData, setTagData] = React.useState(tags);
  const removeTagData = indexToRemove => {
    setTagData([...tagData.filter((_, index) => index !== indexToRemove)]);
  };
  const addTagData = event => {
    if (event.target.value !== '') {
      setTagData([...tagData, event.target.value]);
      event.target.value = '';
    }
  };
  return (
    <div className="tag-input">
      <ul className="tags">
        {tagData.map((tag, index) => (
          <li key={index} className="tag">
            <span className="tag-title">{tag}</span>
            <span
              className="tag-close-icon"
              onClick={() => removeTagData(index)}
            >
              x
            </span>
          </li>
        ))}
      </ul>
      <input
        type="text"
        onKeyUp={event => (event.key === 'Enter' ? addTagData(event) : null)}
        placeholder="Press enter to add a tag"
      />
    </div>
  );
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,34 +1,8 @@

 const TagInput = ({ tags }) => {
-  const [tagData, setTagData] = React.useState(tags);
-  const removeTagData = indexToRemove => {
-    setTagData([...tagData.filter((_, index) => index !== indexToRemove)]);
-  };
-  const addTagData = event => {
-    if (event.target.value !== '') {
-      setTagData([...tagData, event.target.value]);
-      event.target.value = '';
-    }
-  };
-  return (
-    <div className="tag-input">
-      <ul className="tags">
-        {tagData.map((tag, index) => (
-          <li key={index} className="tag">
-            <span className="tag-title">{tag}</span>
-            <span
-              className="tag-close-icon"
-              onClick={() => removeTagData(index)}
-            >
-              x
-            </span>
-          </li>
-        ))}
-      </ul>
-      <input
-        type="text"
-        onKeyUp={event => (event.key === 'Enter' ? addTagData(event) : null)}
-        placeholder="Press enter to add a tag"
-      />
-    </div>
-  );
-};
+  const [input, setInput] = useState('');
+  const [isTagsListOpen, setIsTagsListOpen] = useState(false);
+  const [filteredTags, setFilteredTags] = useState(tags);
+
+  const searchTags = () => {
+    const searchedTags = tags.filter(tag => tag.toLowerCase().includes(input.toLowerCase()));
+    setFilteredTags(se
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,34 +1,13 @@

 const TagInput = ({ tags }) => {
-  const [tagData, setTagData] = React.useState(tags);
-  const removeTagData = indexToRemove => {
-    setTagData([...tagData.filter((_, index) => index !== indexToRemove)]);
+  const [input, setInput] = useState('');
+  const [tagInput, setTagInput] = useState([]);
+
+  const handleChange = (e) => {
+    const { value } = e.target;
+    setInput(value);
   };
-  const addTagData = event => {
-    if (event.target.value !== '') {
-      setTagData([...tagData, event.target.value]);
-      event.target.value = '';
-    }
-  };
-  return (
-    <div className="tag-input">
-      <ul className="tags">
-        {tagData.map((tag, index) => (
-          <li key={index} className="tag">
-            <span className="tag-title">{tag}</span>
-            <span
-              className="tag-close-icon"
-              onClick={() => removeTagData(index)}
-            >
-              x
-            </span>
-          </li>
-        ))}
-      </ul>
-      <input
-        type="text"
-        onKeyUp={event => (event.key === 'Enter' ? addTagData(event) : null)}
-        placeholder="Press enter to add a tag"
-      />
-    </div>
-  );
-};
+
+  const handleKeyPress = (e) => {
+    if (e.key === 'Enter') {
+      e.preventDefault();
+      add
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,34 +1,13 @@

 const TagInput = ({ tags }) => {
-  const [tagData, setTagData] = React.useState(tags);
-  const removeTagData = indexToRemove => {
-    setTagData([...tagData.filter((_, index) => index !== indexToRemove)]);
+  const [text, setText] = useState('');
+  const [tagsArr, setTagsArr] = useState(tags);
+
+  const handleTextChange = event => {
+    setText(event.target.value);
   };
-  const addTagData = event => {
-    if (event.target.value !== '') {
-      setTagData([...tagData, event.target.value]);
-      event.target.value = '';
-    }
-  };
-  return (
-    <div className="tag-input">
-      <ul className="tags">
-        {tagData.map((tag, index) => (
-          <li key={index} className="tag">
-            <span className="tag-title">{tag}</span>
-            <span
-              className="tag-close-icon"
-              onClick={() => removeTagData(index)}
-            >
-              x
-            </span>
-          </li>
-        ))}
-      </ul>
-      <input
-        type="text"
-        onKeyUp={event => (event.key === 'Enter' ? addTagData(event) : null)}
-        placeholder="Press enter to add a tag"
-      />
-    </div>
-  );
-};
+
+  const handleSubmit = event => {
+    event.preventDefault();
+    if (text) {
+      setTagsArr([...tagsArr, text]);
+      set
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,34 +1,13 @@

 const TagInput = ({ tags }) => {
-  const [tagData, setTagData] = React.useState(tags);
-  const removeTagData = indexToRemove => {
-    setTagData([...tagData.filter((_, index) => index !== indexToRemove)]);
+  const [tag, setTag] = useState('');
+  const [tagList, setTagList] = useState(tags);
+
+  const handleTag = (event) => {
+    setTag(event.target.value);
   };
-  const addTagData = event => {
-    if (event.target.value !== '') {
-      setTagData([...tagData, event.target.value]);
-      event.target.value = '';
-    }
-  };
-  return (
-    <div className="tag-input">
-      <ul className="tags">
-        {tagData.map((tag, index) => (
-          <li key={index} className="tag">
-            <span className="tag-title">{tag}</span>
-            <span
-              className="tag-close-icon"
-              onClick={() => removeTagData(index)}
-            >
-              x
-            </span>
-          </li>
-        ))}
-      </ul>
-      <input
-        type="text"
-        onKeyUp={event => (event.key === 'Enter' ? addTagData(event) : null)}
-        placeholder="Press enter to add a tag"
-      />
-    </div>
-  );
-};
+
+  const handleAddTag = () => {
+    if (tag.length > 0) {
+      setTagList([...tagList, tag]);
+      setTag('');
+   
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,34 +1,11 @@

 const TagInput = ({ tags }) => {
-  const [tagData, setTagData] = React.useState(tags);
-  const removeTagData = indexToRemove => {
-    setTagData([...tagData.filter((_, index) => index !== indexToRemove)]);
-  };
-  const addTagData = event => {
-    if (event.target.value !== '') {
-      setTagData([...tagData, event.target.value]);
-      event.target.value = '';
-    }
-  };
-  return (
-    <div className="tag-input">
-      <ul className="tags">
-        {tagData.map((tag, index) => (
-          <li key={index} className="tag">
-            <span className="tag-title">{tag}</span>
-            <span
-              className="tag-close-icon"
-              onClick={() => removeTagData(index)}
-            >
-              x
-            </span>
-          </li>
-        ))}
-      </ul>
-      <input
-        type="text"
-        onKeyUp={event => (event.key === 'Enter' ? addTagData(event) : null)}
-        placeholder="Press enter to add a tag"
-      />
-    </div>
-  );
-};
+  const [ inputValue, setInputValue ] = useState('');
+  const [ active, setActive ] = useState(false);
+  const [ filteredTags, setFilteredTags ] = useState(tags);
+  const [ focus, setFocus ] = useState(false);
+
+  const [ selectedTags, setSelectedTags ] = useState([]);
+
+  const inputRef = useRef(null);
+
+  useEffect(
```

### MultiselectCheckbox (task/20)

#### canonical solution

```javascript
const MultiselectCheckbox = ({ options, onChange }) => {
  const [data, setData] = React.useState(options);

  const toggle = index => {
    const newData = [...data];
    newData.splice(index, 1, {
      label: data[index].label,
      checked: !data[index].checked
    });
    setData(newData);
    onChange(newData.filter(x => x.checked));
  };

  return (
    <>
      {data.map((item, index) => (
        <label key={item.label}>
          <input
            readOnly
            type="checkbox"
            checked={item.checked || false}
            onClick={() => toggle(index)}
          />
          {item.label}
        </label>
      ))}
    </>
  );
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,29 +1,15 @@

 const MultiselectCheckbox = ({ options, onChange }) => {
-  const [data, setData] = React.useState(options);
-
-  const toggle = index => {
-    const newData = [...data];
-    newData.splice(index, 1, {
-      label: data[index].label,
-      checked: !data[index].checked
-    });
-    setData(newData);
-    onChange(newData.filter(x => x.checked));
+  const handleChange = (e) => {
+    onChange(e.target.value);
   };
 
   return (
-    <>
-      {data.map((item, index) => (
-        <label key={item.label}>
-          <input
-            readOnly
-            type="checkbox"
-            checked={item.checked || false}
-            onClick={() => toggle(index)}
-          />
-          {item.label}
-        </label>
-      ))}
-    </>
-  );
-};
+    <div className="multiselect-checkbox">
+      {options.map((option) => (
+        <FormControlLabel
+          key={option.value}
+          control={
+            <Checkbox
+              value={option.value}
+              onChange={handleChange}
+              color="primary"
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,29 +1,15 @@

 const MultiselectCheckbox = ({ options, onChange }) => {
-  const [data, setData] = React.useState(options);
+  const items = options.map(o => ({
+    label: o.label,
+    value: o.value,
+    selected: o.selected,
+  }));
 
-  const toggle = index => {
-    const newData = [...data];
-    newData.splice(index, 1, {
-      label: data[index].label,
-      checked: !data[index].checked
-    });
-    setData(newData);
-    onChange(newData.filter(x => x.checked));
+  const handleSelect = (item, selected) => {
+    onChange(item.value, selected);
   };
 
   return (
-    <>
-      {data.map((item, index) => (
-        <label key={item.label}>
-          <input
-            readOnly
-            type="checkbox"
-            checked={item.checked || false}
-            onClick={() => toggle(index)}
-          />
-          {item.label}
-        </label>
-      ))}
-    </>
-  );
-};
+    <Checkbox.Group
+      className="multiselect-checkbox"
+      onChange={handleSelect}
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,29 +1,14 @@

 const MultiselectCheckbox = ({ options, onChange }) => {
-  const [data, setData] = React.useState(options);
-
-  const toggle = index => {
-    const newData = [...data];
-    newData.splice(index, 1, {
-      label: data[index].label,
-      checked: !data[index].checked
-    });
-    setData(newData);
-    onChange(newData.filter(x => x.checked));
+  const [allSelected, setAllSelected] = useState(false);
+  const onClick = () => {
+    setAllSelected(!allSelected);
+    onChange(allSelected);
   };
 
   return (
-    <>
-      {data.map((item, index) => (
-        <label key={item.label}>
-          <input
-            readOnly
-            type="checkbox"
-            checked={item.checked || false}
-            onClick={() => toggle(index)}
-          />
-          {item.label}
-        </label>
-      ))}
-    </>
-  );
-};
+    <div className="multiselect-checkbox">
+      <input
+        type="checkbox"
+        checked={allSelected}
+        onChange={onClick}
+       
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,29 +1,16 @@

 const MultiselectCheckbox = ({ options, onChange }) => {
-  const [data, setData] = React.useState(options);
-
-  const toggle = index => {
-    const newData = [...data];
-    newData.splice(index, 1, {
-      label: data[index].label,
-      checked: !data[index].checked
-    });
-    setData(newData);
-    onChange(newData.filter(x => x.checked));
+  const handleChange = event => {
+    onChange(event.target.value);
   };
 
   return (
-    <>
-      {data.map((item, index) => (
-        <label key={item.label}>
-          <input
-            readOnly
-            type="checkbox"
-            checked={item.checked || false}
-            onClick={() => toggle(index)}
-          />
-          {item.label}
-        </label>
-      ))}
-    </>
-  );
-};
+    <CheckboxGroup
+      name="form-field-name"
+      value={options}
+      onChange={handleChange}
+    >
+      {options.map(option => (
+        <FormControlLabel
+          value={option}
+          control={<Checkbox color="primary" />}
+          label={
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,29 +1,12 @@

 const MultiselectCheckbox = ({ options, onChange }) => {
-  const [data, setData] = React.useState(options);
+  const [checked, setChecked] = useState({});
 
-  const toggle = index => {
-    const newData = [...data];
-    newData.splice(index, 1, {
-      label: data[index].label,
-      checked: !data[index].checked
-    });
-    setData(newData);
-    onChange(newData.filter(x => x.checked));
+  const onCheck = (value, checked) => {
+    setChecked({ ...checked });
+    onChange(value, checked);
   };
 
   return (
-    <>
-      {data.map((item, index) => (
-        <label key={item.label}>
-          <input
-            readOnly
-            type="checkbox"
-            checked={item.checked || false}
-            onClick={() => toggle(index)}
-          />
-          {item.label}
-        </label>
-      ))}
-    </>
-  );
-};
+    <div className="checkbox-group">
+      {options.map(({ label, value }) => (
+        <div className="checkbox-group__item" key={value}>
```

### DataList (task/21)

#### canonical solution

```javascript
const DataList = ({ isOrdered = false, data }) => {
  const list = data.map((val, i) => <li key={`${i}_${val}`}>{val}</li>);
  return isOrdered ? <ol>{list}</ol> : <ul>{list}</ul>;
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,4 +1,9 @@

 const DataList = ({ isOrdered = false, data }) => {
-  const list = data.map((val, i) => <li key={`${i}_${val}`}>{val}</li>);
-  return isOrdered ? <ol>{list}</ol> : <ul>{list}</ul>;
-};
+  const renderRows = () => {
+    return data.map((item, index) => {
+      return (
+        <li className="data-list__item" key={`${item}_${index}`}>
+          {item}
+        </li>
+      );
+    });
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,4 +1,9 @@

 const DataList = ({ isOrdered = false, data }) => {
-  const list = data.map((val, i) => <li key={`${i}_${val}`}>{val}</li>);
-  return isOrdered ? <ol>{list}</ol> : <ul>{list}</ul>;
-};
+  return (
+    <div className="datalist">
+      {data.map((item, i) => (
+        <div key={i} className="datalist-item">
+          <div className="datalist-item-text">
+            {isOrdered ? (
+              <OrderItem data={item} />
+            ) : (
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,4 +1,8 @@

 const DataList = ({ isOrdered = false, data }) => {
-  const list = data.map((val, i) => <li key={`${i}_${val}`}>{val}</li>);
-  return isOrdered ? <ol>{list}</ol> : <ul>{list}</ul>;
-};
+  const dataList = data.map((dataRow, index) => {
+    const className = index === 0 ? 'DataList_DataRow_First' : '';
+    const isOrderedData =
+      dataRow.orderedData && dataRow.orderedData.length > 0;
+    const data = isOrderedData ? dataRow.orderedData : dataRow.unorderedData;
+    return (
+      <li key={data
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,4 +1,8 @@

 const DataList = ({ isOrdered = false, data }) => {
-  const list = data.map((val, i) => <li key={`${i}_${val}`}>{val}</li>);
-  return isOrdered ? <ol>{list}</ol> : <ul>{list}</ul>;
+  const ordered = <ol>{data.map(DataListItem)}</ol>;
+  const unordered = <ul>{data.map(DataListItem)}</ul>;
+
+  return isOrdered ? ordered : unordered;
 };
+
+export default DataList;
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,4 +1,9 @@

 const DataList = ({ isOrdered = false, data }) => {
-  const list = data.map((val, i) => <li key={`${i}_${val}`}>{val}</li>);
-  return isOrdered ? <ol>{list}</ol> : <ul>{list}</ul>;
-};
+  const renderHeader = isOrdered ? <OrderedListHeader /> : <ListHeader />;
+  const renderItem = isOrdered ? <OrderedListItem /> : <ListItem />;
+
+  return (
+    <ul className="list">
+      {renderHeader}
+      {data.map((item, index) => (
+        <li key={index}>{renderItem(item)}</li>
```

### Carousel (task/22)

#### canonical solution

```javascript
const Carousel = ({ carouselItems, ...rest }) => {
  const [active, setActive] = React.useState(0);
  let scrollInterval = null;

  React.useEffect(() => {
    scrollInterval = setTimeout(() => {
      setActive((active + 1) % carouselItems.length);
    }, 2000);
    return () => clearTimeout(scrollInterval);
  });

  return (
    <div className="carousel">
      {carouselItems.map((item, index) => {
        const activeClass = active === index ? ' visible' : '';
        return React.cloneElement(item, {
          ...rest,
          className: `carousel-item${activeClass}`
        });
      })}
    </div>
  );
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,23 +1,11 @@

 const Carousel = ({ carouselItems, ...rest }) => {
-  const [active, setActive] = React.useState(0);
-  let scrollInterval = null;
+  const [currentIdx, setCurrentIdx] = useState(0);
+  const [translateValue, setTranslateValue] = useState(0);
+  const { width } = useWindowDimensions();
 
-  React.useEffect(() => {
-    scrollInterval = setTimeout(() => {
-      setActive((active + 1) % carouselItems.length);
-    }, 2000);
-    return () => clearTimeout(scrollInterval);
-  });
+  useEffect(() => {
+    setTranslateValue(width * currentIdx);
+  }, [currentIdx, width]);
 
-  return (
-    <div className="carousel">
-      {carouselItems.map((item, index) => {
-        const activeClass = active === index ? ' visible' : '';
-        return React.cloneElement(item, {
-          ...rest,
-          className: `carousel-item${activeClass}`
-        });
-      })}
-    </div>
-  );
-};
+  const nextSlide = () => {
+    if (currentIdx ===
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,23 +1,9 @@

 const Carousel = ({ carouselItems, ...rest }) => {
-  const [active, setActive] = React.useState(0);
-  let scrollInterval = null;
+  const { t } = useTranslation();
+  const classes = useStyles();
+  const [carouselIndex, setCarouselIndex] = useState(0);
+  const [carouselTranslateValue, setCarouselTranslateValue] = useState(0);
+  const [animationValue, setAnimationValue] = useState(new Animated.Value(0));
 
-  React.useEffect(() => {
-    scrollInterval = setTimeout(() => {
-      setActive((active + 1) % carouselItems.length);
-    }, 2000);
-    return () => clearTimeout(scrollInterval);
-  });
-
-  return (
-    <div className="carousel">
-      {carouselItems.map((item, index) => {
-        const activeClass = active === index ? ' visible' : '';
-        return React.cloneElement(item, {
-          ...rest,
-          className: `carousel-item${activeClass}`
-        });
-      })}
-    </div>
-  );
-};
+  const renderCarouselItems = () => {
+    return car
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,23 +1,7 @@

 const Carousel = ({ carouselItems, ...rest }) => {
-  const [active, setActive] = React.useState(0);
-  let scrollInterval = null;
-
-  React.useEffect(() => {
-    scrollInterval = setTimeout(() => {
-      setActive((active + 1) % carouselItems.length);
-    }, 2000);
-    return () => clearTimeout(scrollInterval);
-  });
-
-  return (
-    <div className="carousel">
-      {carouselItems.map((item, index) => {
-        const activeClass = active === index ? ' visible' : '';
-        return React.cloneElement(item, {
-          ...rest,
-          className: `carousel-item${activeClass}`
-        });
-      })}
-    </div>
-  );
-};
+  const [currentSlide, setCurrentSlide] = useState(0);
+  const [slideWidth, setSlideWidth] = useState(0);
+  const [slideHeight, setSlideHeight] = useState(0);
+  const [visibleSlides, setVisibleSlides] = useState(3);
+  const { width, height } = useViewport();
+  const { theme } = useTheme
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,23 +1,14 @@

 const Carousel = ({ carouselItems, ...rest }) => {
-  const [active, setActive] = React.useState(0);
-  let scrollInterval = null;
-
-  React.useEffect(() => {
-    scrollInterval = setTimeout(() => {
-      setActive((active + 1) % carouselItems.length);
-    }, 2000);
-    return () => clearTimeout(scrollInterval);
+  const renderItems = carouselItems.map((item, index) => {
+    return (
+      <CarouselItem key={index} {...item} {...rest}>
+        {item.children}
+      </CarouselItem>
+    );
   });
 
-  return (
-    <div className="carousel">
-      {carouselItems.map((item, index) => {
-        const activeClass = active === index ? ' visible' : '';
-        return React.cloneElement(item, {
-          ...rest,
-          className: `carousel-item${activeClass}`
-        });
-      })}
-    </div>
-  );
+  return <CarouselWrapper {...rest}>{renderItems}</CarouselWrapper>;
 };
+
+Carousel.propTypes = {
+  car
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,23 +1,16 @@

 const Carousel = ({ carouselItems, ...rest }) => {
-  const [active, setActive] = React.useState(0);
-  let scrollInterval = null;
-
-  React.useEffect(() => {
-    scrollInterval = setTimeout(() => {
-      setActive((active + 1) % carouselItems.length);
-    }, 2000);
-    return () => clearTimeout(scrollInterval);
-  });
+  const settings = {
+    dots: true,
+    speed: 500,
+    slidesToShow: 1,
+    slidesToScroll: 1,
+    autoplay: true,
+    autoplaySpeed: 5000,
+    ...rest,
+  };
 
   return (
-    <div className="carousel">
-      {carouselItems.map((item, index) => {
-        const activeClass = active === index ? ' visible' : '';
-        return React.cloneElement(item, {
-          ...rest,
-          className: `carousel-item${activeClass}`
-        });
-      })}
-    </div>
-  );
-};
+    <CarouselContainer>
+      <Slider {...settings}>
+        {carouselItems.map((item) => (
+          <div key={item.
```

### useMergeState (task/23)

#### canonical solution

```javascript
const useMergeState = (initialState = {}) => {
  const [value, setValue] = React.useState(initialState);

  const mergeState = newState => {
    if (typeof newState === 'function') newState = newState(value);
    setValue({ ...value, ...newState });
  };

  return [value, mergeState];
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,10 +1,12 @@

 const useMergeState = (initialState = {}) => {
-  const [value, setValue] = React.useState(initialState);
+  const [state, setState] = useState(initialState);
 
-  const mergeState = newState => {
-    if (typeof newState === 'function') newState = newState(value);
-    setValue({ ...value, ...newState });
+  const setMergeState = (newState) => {
+    const updateState = (s, n) => ({ ...s, ...n });
+    setState((prevState) => updateState(prevState, newState));
   };
 
-  return [value, mergeState];
+  return [state, setMergeState];
 };
+
+export default useMergeState;
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,10 +1,11 @@

 const useMergeState = (initialState = {}) => {
-  const [value, setValue] = React.useState(initialState);
+  const [state, setState] = useState(initialState);
+  const stateMerge = useCallback((newState) => {
+    setState((prevState) => {
+      return { ...prevState, ...newState };
+    });
+  }, []);
+  return [state, stateMerge];
+};
 
-  const mergeState = newState => {
-    if (typeof newState === 'function') newState = newState(value);
-    setValue({ ...value, ...newState });
-  };
-
-  return [value, mergeState];
-};
+export default useMergeState;
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,10 +1,11 @@

 const useMergeState = (initialState = {}) => {
-  const [value, setValue] = React.useState(initialState);
+  const [state, setState] = useState(initialState);
+  const setMergeState = (newState) => {
+    setState({ ...state, ...newState });
+  };
+  return [state, setMergeState];
+};
 
-  const mergeState = newState => {
-    if (typeof newState === 'function') newState = newState(value);
-    setValue({ ...value, ...newState });
-  };
-
-  return [value, mergeState];
-};
+const useSyncState = (initialState = {}) => {
+  const [state, setState] = useState(initialState);
+  const setSyncState = (newState
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,10 +1,6 @@

 const useMergeState = (initialState = {}) => {
-  const [value, setValue] = React.useState(initialState);
+  const mergeRef = useRef(initialState);
+  return useMemo(() => [mergeRef.current, mergeRef.current.set, mergeRef.current.delete], [initialState]);
+};
 
-  const mergeState = newState => {
-    if (typeof newState === 'function') newState = newState(value);
-    setValue({ ...value, ...newState });
-  };
-
-  return [value, mergeState];
-};
+export default useMergeState;
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,10 +1,14 @@

 const useMergeState = (initialState = {}) => {
-  const [value, setValue] = React.useState(initialState);
+  const [state, setState] = useState(initialState);
 
-  const mergeState = newState => {
-    if (typeof newState === 'function') newState = newState(value);
-    setValue({ ...value, ...newState });
+  const setValue = (key, value) => {
+    setState({
+      ...state,
+      [key]: value,
+    });
   };
 
-  return [value, mergeState];
+  return [state, setValue];
 };
+
+export default useMergeState;
```

### useAsync (task/24)

#### canonical solution

```javascript
const useAsync = fn => {
  const initialState = { loading: false, error: null, value: null };
  const stateReducer = (_, action) => {
    switch (action.type) {
      case 'start':
        return { loading: true, error: null, value: null };
      case 'finish':
        return { loading: false, error: null, value: action.value };
      case 'error':
        return { loading: false, error: action.error, value: null };
    }
  };

  const [state, dispatch] = React.useReducer(stateReducer, initialState);

  const run = async (args = null) => {
    try {
      dispatch({ type: 'start' });
      const value = await fn(args);
      dispatch({ type: 'finish', value });
    } catch (error) {
      dispatch({ type: 'error', error });
    }
  };

  return { ...state, run };
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,27 +1,19 @@

 const useAsync = fn => {
-  const initialState = { loading: false, error: null, value: null };
-  const stateReducer = (_, action) => {
-    switch (action.type) {
-      case 'start':
-        return { loading: true, error: null, value: null };
-      case 'finish':
-        return { loading: false, error: null, value: action.value };
-      case 'error':
-        return { loading: false, error: action.error, value: null };
-    }
-  };
+  const [state, setState] = useState({
+    loading: false,
+    data: null,
+    error: null,
+  });
 
-  const [state, dispatch] = React.useReducer(stateReducer, initialState);
+  useEffect(() => {
+    async function load() {
+      setState({
+        loading: true,
+        data: null,
+        error: null,
+      });
 
-  const run = async (args = null) => {
-    try {
-      dispatch({ type: 'start' });
-      const value = await fn(args);
-      dispatch({ type: 'finish', value });
-    } catch (error) {
-      dispatch({ type: 'error', error });
-    }
-  };
-
-  return { ...state, run };
-};
+      try {
+        const result = await fn();
+        setState({
+          loading: false,
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,27 +1,13 @@

 const useAsync = fn => {
-  const initialState = { loading: false, error: null, value: null };
-  const stateReducer = (_, action) => {
-    switch (action.type) {
-      case 'start':
-        return { loading: true, error: null, value: null };
-      case 'finish':
-        return { loading: false, error: null, value: action.value };
-      case 'error':
-        return { loading: false, error: action.error, value: null };
-    }
-  };
+  const [loading, setLoading] = useState(false);
+  const [error, setError] = useState(null);
+  const [result, setResult] = useState(null);
 
-  const [state, dispatch] = React.useReducer(stateReducer, initialState);
-
-  const run = async (args = null) => {
-    try {
-      dispatch({ type: 'start' });
-      const value = await fn(args);
-      dispatch({ type: 'finish', value });
-    } catch (error) {
-      dispatch({ type: 'error', error });
-    }
-  };
-
-  return { ...state, run };
-};
+  useEffect(() => {
+    async function doFetch() {
+      setLoading(true);
+      try {
+        const result = await fn();
+        setResult(result);
+      } catch (error) {
+        set
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,27 +1,8 @@

 const useAsync = fn => {
-  const initialState = { loading: false, error: null, value: null };
-  const stateReducer = (_, action) => {
-    switch (action.type) {
-      case 'start':
-        return { loading: true, error: null, value: null };
-      case 'finish':
-        return { loading: false, error: null, value: action.value };
-      case 'error':
-        return { loading: false, error: action.error, value: null };
-    }
-  };
+  const wrapper = useCallback(async (...args) => {
+    await fn(...args);
+  }, []);
+  return wrapper;
+};
 
-  const [state, dispatch] = React.useReducer(stateReducer, initialState);
-
-  const run = async (args = null) => {
-    try {
-      dispatch({ type: 'start' });
-      const value = await fn(args);
-      dispatch({ type: 'finish', value });
-    } catch (error) {
-      dispatch({ type: 'error', error });
-    }
-  };
-
-  return { ...state, run };
-};
+export default useAsync;
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,27 +1,12 @@

 const useAsync = fn => {
-  const initialState = { loading: false, error: null, value: null };
-  const stateReducer = (_, action) => {
-    switch (action.type) {
-      case 'start':
-        return { loading: true, error: null, value: null };
-      case 'finish':
-        return { loading: false, error: null, value: action.value };
-      case 'error':
-        return { loading: false, error: action.error, value: null };
-    }
+  return () => {
+    const controller = new AbortController();
+    const [value, error] = useAsyncError(fn, controller.signal);
+    const abort = () => controller.abort();
+    return { value, error, abort };
   };
+};
 
-  const [state, dispatch] = React.useReducer(stateReducer, initialState);
-
-  const run = async (args = null) => {
-    try {
-      dispatch({ type: 'start' });
-      const value = await fn(args);
-      dispatch({ type: 'finish', value });
-    } catch (error) {
-      dispatch({ type: 'error', error });
-    }
-  };
-
-  return { ...state, run };
-};
+export const useAsyncWithAbort = (fn, ctx) => {
+  const controller = new AbortController();
+  const [value, error]
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,27 +1,16 @@

 const useAsync = fn => {
-  const initialState = { loading: false, error: null, value: null };
-  const stateReducer = (_, action) => {
-    switch (action.type) {
-      case 'start':
-        return { loading: true, error: null, value: null };
-      case 'finish':
-        return { loading: false, error: null, value: action.value };
-      case 'error':
-        return { loading: false, error: action.error, value: null };
-    }
-  };
+  const [state, setState] = useState(INITIAL_STATE);
 
-  const [state, dispatch] = React.useReducer(stateReducer, initialState);
-
-  const run = async (args = null) => {
+  const execute = async () => {
+    setState(PENDING_STATE);
     try {
-      dispatch({ type: 'start' });
-      const value = await fn(args);
-      dispatch({ type: 'finish', value });
+      const result = await fn();
+      setState({
+        data: result,
+        isValid: true,
+      });
     } catch (error) {
-      dispatch({ type: 'error', error });
-    }
-  };
-
-  return { ...state, run };
-};
+      setState({
+        error,
+        isValid: false,
+      });
```

### useBodyScrollLock (task/25)

#### canonical solution

```javascript
const useBodyScrollLock = () => {
  React.useLayoutEffect(() => {
    const originalStyle = window.getComputedStyle(document.body).overflow;
    document.body.style.overflow = 'hidden';
    return () => (document.body.style.overflow = originalStyle);
  }, []);
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,7 +1,9 @@

 const useBodyScrollLock = () => {
-  React.useLayoutEffect(() => {
-    const originalStyle = window.getComputedStyle(document.body).overflow;
-    document.body.style.overflow = 'hidden';
-    return () => (document.body.style.overflow = originalStyle);
-  }, []);
-};
+  useEffect(() => {
+    const scrollHandler = () => {
+      const scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
+      const height = document.documentElement.scrollHeight || document.body.scrollHeight;
+      const offset = window.innerHeight;
+      if (scrollTop + offset >= height) {
+        document.body.style.overflow = 'hidden';
+      } else {
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,7 +1,12 @@

 const useBodyScrollLock = () => {
-  React.useLayoutEffect(() => {
-    const originalStyle = window.getComputedStyle(document.body).overflow;
-    document.body.style.overflow = 'hidden';
-    return () => (document.body.style.overflow = originalStyle);
+  const [isLocked, setIsLocked] = useState(false);
+
+  const onScrollHandler = useCallback(() => {
+    setIsLocked(window.scrollY > 0);
   }, []);
-};
+
+  useEffect(() => {
+    window.addEventListener('scroll', onScrollHandler);
+
+    return () => {
+      window.removeEventListener('scroll', onScrollHandler);
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,7 +1,12 @@

 const useBodyScrollLock = () => {
-  React.useLayoutEffect(() => {
-    const originalStyle = window.getComputedStyle(document.body).overflow;
-    document.body.style.overflow = 'hidden';
-    return () => (document.body.style.overflow = originalStyle);
+  const [ref, setRef] = useState<HTMLDivElement | null>(null);
+  const [isFixed, setIsFixed] = useState(false);
+
+  const elRef = useCallback((node: HTMLDivElement) => {
+    if (node !== null) {
+      setRef(node);
+    }
   }, []);
-};
+
+  const handleScroll = useCallback(() => {
+    if (ref && ref
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,7 +1,12 @@

 const useBodyScrollLock = () => {
-  React.useLayoutEffect(() => {
-    const originalStyle = window.getComputedStyle(document.body).overflow;
-    document.body.style.overflow = 'hidden';
-    return () => (document.body.style.overflow = originalStyle);
-  }, []);
-};
+    const html = document.querySelector('html');
+    const body = document.querySelector('body');
+    const lock = () => {
+        html.style.overflow = 'hidden';
+        body.style.overflow = 'hidden';
+    };
+    const unlock = () => {
+        html.style.overflow = '';
+        body.style.overflow = '';
+    };
+    return {
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,7 +1,12 @@

 const useBodyScrollLock = () => {
-  React.useLayoutEffect(() => {
-    const originalStyle = window.getComputedStyle(document.body).overflow;
-    document.body.style.overflow = 'hidden';
-    return () => (document.body.style.overflow = originalStyle);
-  }, []);
-};
+  return {
+    bind: {
+      style: {
+        position: 'fixed',
+        width: '100%',
+        height: '100%',
+        top: 0,
+        left: 0,
+        right: 0,
+        bottom: 0,
+        margin: 0,
```

### useForm (task/26)

#### canonical solution

```javascript
const useForm = initialValues => {
  const [values, setValues] = React.useState(initialValues);

  return [
    values,
    e => {
      setValues({
        ...values,
        [e.target.name]: e.target.value
      });
    }
  ];
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,13 +1,18 @@

 const useForm = initialValues => {
-  const [values, setValues] = React.useState(initialValues);
+  const [values, setValues] = useState(initialValues);
 
-  return [
+  const handleInputChange = ({ target: { name, value } }) => {
+    setValues({ ...values, [name]: value });
+  };
+
+  const handleSubmit = event => {
+    if (event) event.preventDefault();
+  };
+
+  return {
     values,
-    e => {
-      setValues({
-        ...values,
-        [e.target.name]: e.target.value
-      });
-    }
-  ];
+    handleInputChange,
+    handleSubmit
+  };
 };
+
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,13 +1,17 @@

 const useForm = initialValues => {
-  const [values, setValues] = React.useState(initialValues);
+  const [values, setValues] = useState(initialValues);
 
-  return [
-    values,
-    e => {
-      setValues({
-        ...values,
-        [e.target.name]: e.target.value
-      });
-    }
-  ];
-};
+  const handleChange = e => {
+    const { name, value } = e.target;
+    setValues({ ...values, [name]: value });
+  };
+
+  const handleSubmit = e => {
+    e.preventDefault();
+    console.log(values);
+  };
+
+  return {
+    handleChange,
+    handleSubmit,
+    values
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,13 +1,18 @@

 const useForm = initialValues => {
-  const [values, setValues] = React.useState(initialValues);
+  const [values, setValues] = useState(initialValues);
 
-  return [
-    values,
-    e => {
-      setValues({
-        ...values,
-        [e.target.name]: e.target.value
-      });
-    }
-  ];
-};
+  const handleInputChange = e => {
+    setValues({
+      ...values,
+      [e.target.name]: e.target.value
+    });
+  };
+
+  const handleSubmit = e => {
+    e.preventDefault();
+    console.log(values);
+  };
+
+  return {
+    handleInputChange,
+    handleSubmit,
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,13 +1,17 @@

 const useForm = initialValues => {
-  const [values, setValues] = React.useState(initialValues);
+  const [values, setValues] = useState(initialValues);
 
-  return [
-    values,
-    e => {
-      setValues({
-        ...values,
-        [e.target.name]: e.target.value
-      });
-    }
-  ];
-};
+  const handleChange = e => {
+    setValues({
+      ...values,
+      [e.target.name]: e.target.value
+    });
+  };
+
+  const handleSubmit = e => {
+    e.preventDefault();
+    alert(JSON.stringify(values, null, 2));
+  };
+
+  return {
+    handleChange,
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,13 +1,14 @@

 const useForm = initialValues => {
-  const [values, setValues] = React.useState(initialValues);
+  const [formState, setFormState] = useState(initialValues);
 
-  return [
-    values,
-    e => {
-      setValues({
-        ...values,
-        [e.target.name]: e.target.value
-      });
-    }
-  ];
-};
+  const handleInputChange = (event) => {
+    event.persist();
+    setFormState(state => ({
+      ...state,
+      [event.target.name]: event.target.value,
+    }));
+  };
+
+  const handleSubmit = (event) => {
+    event.preventDefault();
+    setFormState(initial
```

### usePortal (task/27)

#### canonical solution

```javascript
const usePortal = el => {
  const [portal, setPortal] = React.useState({
    render: () => null,
    remove: () => null,
  });

  const createPortal = React.useCallback(el => {
    const Portal = ({ children }) => ReactDOM.createPortal(children, el);
    const remove = () => ReactDOM.unmountComponentAtNode(el);
    return { render: Portal, remove };
  }, []);

  React.useEffect(() => {
    if (el) portal.remove();
    const newPortal = createPortal(el);
    setPortal(newPortal);
    return () => newPortal.remove(el);
  }, [el]);

  return portal.render;
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,21 +1,12 @@

 const usePortal = el => {
-  const [portal, setPortal] = React.useState({
-    render: () => null,
-    remove: () => null,
-  });
-
-  const createPortal = React.useCallback(el => {
-    const Portal = ({ children }) => ReactDOM.createPortal(children, el);
-    const remove = () => ReactDOM.unmountComponentAtNode(el);
-    return { render: Portal, remove };
+  const portalRef = useRef(null);
+  useEffect(() => {
+    portalRef.current = document.createElement('div');
+    document.body.appendChild(portalRef.current);
+    return () => {
+      document.body.removeChild(portalRef.current);
+    };
   }, []);
-
-  React.useEffect(() => {
-    if (el) portal.remove();
-    const newPortal = createPortal(el);
-    setPortal(newPortal);
-    return () => newPortal.remove(el);
-  }, [el]);
-
-  return portal.render;
-};
+  useEffect(() => {
+    if (portalRef.current) {
+      portal
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,21 +1,13 @@

 const usePortal = el => {
-  const [portal, setPortal] = React.useState({
-    render: () => null,
-    remove: () => null,
-  });
+	const [target, setTarget] = useState(null);
+	const [container] = useState(document.createElement("div"));
 
-  const createPortal = React.useCallback(el => {
-    const Portal = ({ children }) => ReactDOM.createPortal(children, el);
-    const remove = () => ReactDOM.unmountComponentAtNode(el);
-    return { render: Portal, remove };
-  }, []);
+	useEffect(() => {
+		const { current } = el;
+		setTarget(current);
+	}, [el]);
 
-  React.useEffect(() => {
-    if (el) portal.remove();
-    const newPortal = createPortal(el);
-    setPortal(newPortal);
-    return () => newPortal.remove(el);
-  }, [el]);
-
-  return portal.render;
-};
+	useEffect(() => {
+		const { current } = target;
+		current.appendChild(container);
+		return () =>
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,21 +1,15 @@

 const usePortal = el => {
-  const [portal, setPortal] = React.useState({
-    render: () => null,
-    remove: () => null,
-  });
+  const [portal, setPortal] = useState(null);
+  const [modal, setModal] = useState(false);
 
-  const createPortal = React.useCallback(el => {
-    const Portal = ({ children }) => ReactDOM.createPortal(children, el);
-    const remove = () => ReactDOM.unmountComponentAtNode(el);
-    return { render: Portal, remove };
-  }, []);
-
-  React.useEffect(() => {
-    if (el) portal.remove();
-    const newPortal = createPortal(el);
-    setPortal(newPortal);
-    return () => newPortal.remove(el);
+  useEffect(() => {
+    const mountNode = document.getElementById(el);
+    if (mountNode) {
+      setPortal(mountNode);
+    }
   }, [el]);
 
-  return portal.render;
+  return [portal, setModal];
 };
+
+export default
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,21 +1,12 @@

 const usePortal = el => {
-  const [portal, setPortal] = React.useState({
-    render: () => null,
-    remove: () => null,
-  });
+  const [portal, setPortal] = useState(false);
+  const togglePortal = () => setPortal(!portal);
+  const portalRoot = usePortalRoot();
 
-  const createPortal = React.useCallback(el => {
-    const Portal = ({ children }) => ReactDOM.createPortal(children, el);
-    const remove = () => ReactDOM.unmountComponentAtNode(el);
-    return { render: Portal, remove };
-  }, []);
-
-  React.useEffect(() => {
-    if (el) portal.remove();
-    const newPortal = createPortal(el);
-    setPortal(newPortal);
-    return () => newPortal.remove(el);
-  }, [el]);
-
-  return portal.render;
-};
+  if (portalRoot) {
+    return createPortal(
+      <PortalContext.Provider value={{ portal, togglePortal }}>
+        {el}
+      </PortalContext.Provider>,
+      portalRoot
+   
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,21 +1,12 @@

 const usePortal = el => {
-  const [portal, setPortal] = React.useState({
-    render: () => null,
-    remove: () => null,
-  });
+  const existing = useRef(document.querySelector(el));
+  const [portal] = useState(document.createElement('div'));
 
-  const createPortal = React.useCallback(el => {
-    const Portal = ({ children }) => ReactDOM.createPortal(children, el);
-    const remove = () => ReactDOM.unmountComponentAtNode(el);
-    return { render: Portal, remove };
-  }, []);
-
-  React.useEffect(() => {
-    if (el) portal.remove();
-    const newPortal = createPortal(el);
-    setPortal(newPortal);
-    return () => newPortal.remove(el);
-  }, [el]);
-
-  return portal.render;
-};
+  useEffect(() => {
+    if (existing.current) {
+      existing.current.parentNode.removeChild(existing.current);
+    }
+    document.body.appendChild(portal);
+    return () => {
+      portal.remove();
+    };
```

### Mailto (task/28)

#### canonical solution

```javascript
const Mailto = ({ email, subject = '', body = '', children }) => {
  let params = subject || body ? '?' : '';
  if (subject) params += `subject=${encodeURIComponent(subject)}`;
  if (body) params += `${subject ? '&' : ''}body=${encodeURIComponent(body)}`;

  return <a href={`mailto:${email}${params}`}>{children}</a>;
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,7 +1,8 @@

 const Mailto = ({ email, subject = '', body = '', children }) => {
-  let params = subject || body ? '?' : '';
-  if (subject) params += `subject=${encodeURIComponent(subject)}`;
-  if (body) params += `${subject ? '&' : ''}body=${encodeURIComponent(body)}`;
-
-  return <a href={`mailto:${email}${params}`}>{children}</a>;
-};
+  const [anchorRef, isOpen] = useToggle(false);
+  const linkProps = {
+    ...(href || (email && `mailto:${email}`)),
+    ...(onClick && { onClick }),
+    ...(target && { target }),
+    ...(rel && { rel }),
+    ...(tabIndex === undefined ? { tabIndex: '-1' } : { tabIndex }
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,7 +1,8 @@

 const Mailto = ({ email, subject = '', body = '', children }) => {
-  let params = subject || body ? '?' : '';
-  if (subject) params += `subject=${encodeURIComponent(subject)}`;
-  if (body) params += `${subject ? '&' : ''}body=${encodeURIComponent(body)}`;
-
-  return <a href={`mailto:${email}${params}`}>{children}</a>;
-};
+  const qs = [];
+  if (subject) qs.push(`subject=${encodeURIComponent(subject)}`);
+  if (body) qs.push(`body=${encodeURIComponent(body)}`);
+  return (
+    <a href={`mailto:${email}?${qs.join('&')}`}>
+      {children}
+    </a>
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,7 +1,12 @@

 const Mailto = ({ email, subject = '', body = '', children }) => {
-  let params = subject || body ? '?' : '';
-  if (subject) params += `subject=${encodeURIComponent(subject)}`;
-  if (body) params += `${subject ? '&' : ''}body=${encodeURIComponent(body)}`;
+  return (
+    <a
+      href={`mailto:${email}?subject=${subject}&body=${body}`}
+      onClick={() => trackEvent('clicked_email', { subject, body })}
+    >
+      {children}
+    </a>
+  )
+}
 
-  return <a href={`mailto:${email}${params}`}>{children}</a>;
-};
+export default Mailto
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,7 +1,12 @@

 const Mailto = ({ email, subject = '', body = '', children }) => {
-  let params = subject || body ? '?' : '';
-  if (subject) params += `subject=${encodeURIComponent(subject)}`;
-  if (body) params += `${subject ? '&' : ''}body=${encodeURIComponent(body)}`;
-
-  return <a href={`mailto:${email}${params}`}>{children}</a>;
-};
+  const href = `mailto:${email}?subject=${subject}&body=${body}`;
+  return (
+    <a
+      href={href}
+      target="_blank"
+      rel="noopener noreferrer"
+      className="mailto-link"
+    >
+      {children}
+    </a>
+  );
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,7 +1,12 @@

 const Mailto = ({ email, subject = '', body = '', children }) => {
-  let params = subject || body ? '?' : '';
-  if (subject) params += `subject=${encodeURIComponent(subject)}`;
-  if (body) params += `${subject ? '&' : ''}body=${encodeURIComponent(body)}`;
-
-  return <a href={`mailto:${email}${params}`}>{children}</a>;
-};
+  const href = `mailto:${email}?subject=${subject}&body=${body}`;
+  return (
+    <a
+      className="mailto"
+      href={href}
+      target="_blank"
+      rel="noopener noreferrer"
+    >
+      {children}
+    </a>
+  );
```

### useKeyPress (task/29)

#### canonical solution

```javascript
const useKeyPress = targetKey => {
  const [keyPressed, setKeyPressed] = React.useState(false);

  const downHandler = ({ key }) => {
    if (key === targetKey) setKeyPressed(true);
  };

  const upHandler = ({ key }) => {
    if (key === targetKey) setKeyPressed(false);
  };

  React.useEffect(() => {
    window.addEventListener('keydown', downHandler);
    window.addEventListener('keyup', upHandler);

    return () => {
      window.removeEventListener('keydown', downHandler);
      window.removeEventListener('keyup', upHandler);
    };
  }, []);

  return keyPressed;
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,23 +1,16 @@

 const useKeyPress = targetKey => {
-  const [keyPressed, setKeyPressed] = React.useState(false);
+  const listener = event => {
+    if (event.key === targetKey) {
+      // console.log(targetKey);
+      return false;
+    }
+  };
+  useEffect(() => {
+    window.addEventListener("keydown", listener);
+    return () => {
+      window.removeEventListener("keydown", listener);
+    };
+  });
+};
 
-  const downHandler = ({ key }) => {
-    if (key === targetKey) setKeyPressed(true);
-  };
-
-  const upHandler = ({ key }) => {
-    if (key === targetKey) setKeyPressed(false);
-  };
-
-  React.useEffect(() => {
-    window.addEventListener('keydown', downHandler);
-    window.addEventListener('keyup', upHandler);
-
-    return () => {
-      window.removeEventListener('keydown', downHandler);
-      window.removeEventListener('keyup', upHandler);
-    };
-  }, []);
-
-  return keyPressed;
-};
+export default useKeyPress;
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,23 +1,16 @@

 const useKeyPress = targetKey => {
-  const [keyPressed, setKeyPressed] = React.useState(false);
+  const [keyPressed, setKeyPressed] = useState(false);
 
   const downHandler = ({ key }) => {
-    if (key === targetKey) setKeyPressed(true);
+    if (key === targetKey) {
+      setKeyPressed(true);
+    }
   };
 
   const upHandler = ({ key }) => {
-    if (key === targetKey) setKeyPressed(false);
+    if (key === targetKey) {
+      setKeyPressed(false);
+    }
   };
 
-  React.useEffect(() => {
-    window.addEventListener('keydown', downHandler);
-    window.addEventListener('keyup', upHandler);
-
-    return () => {
-      window.removeEventListener('keydown', downHandler);
-      window.removeEventListener('keyup', upHandler);
-    };
-  }, []);
-
-  return keyPressed;
-};
+  useEffect(() => {
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,23 +1,14 @@

 const useKeyPress = targetKey => {
-  const [keyPressed, setKeyPressed] = React.useState(false);
+	const [keyPressed, setKeyPressed] = useState(false);
 
-  const downHandler = ({ key }) => {
-    if (key === targetKey) setKeyPressed(true);
-  };
+	const downHandler = ({ key }) => {
+		if (key === targetKey) {
+			setKeyPressed(true);
+		}
+	};
 
-  const upHandler = ({ key }) => {
-    if (key === targetKey) setKeyPressed(false);
-  };
-
-  React.useEffect(() => {
-    window.addEventListener('keydown', downHandler);
-    window.addEventListener('keyup', upHandler);
-
-    return () => {
-      window.removeEventListener('keydown', downHandler);
-      window.removeEventListener('keyup', upHandler);
-    };
-  }, []);
-
-  return keyPressed;
-};
+	const upHandler = ({ key }) => {
+		if (key === targetKey) {
+			setKeyPressed(false);
+		}
+	};
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,23 +1,13 @@

 const useKeyPress = targetKey => {
-  const [keyPressed, setKeyPressed] = React.useState(false);
+  // State for keeping track of whether key is pressed
+  const [keyPressed, setKeyPressed] = useState(false);
 
-  const downHandler = ({ key }) => {
-    if (key === targetKey) setKeyPressed(true);
-  };
+  // If pressed key is our target key then set to true
+  function downHandler({ key }) {
+    if (key === targetKey) {
+      setKeyPressed(true);
+    }
+  }
 
-  const upHandler = ({ key }) => {
-    if (key === targetKey) setKeyPressed(false);
-  };
-
-  React.useEffect(() => {
-    window.addEventListener('keydown', downHandler);
-    window.addEventListener('keyup', upHandler);
-
-    return () => {
-      window.removeEventListener('keydown', downHandler);
-      window.removeEventListener('keyup', upHandler);
-    };
-  }, []);
-
-  return keyPressed;
-};
+  // If released key is our target key then set to false
+  const upHandler =
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,23 +1,16 @@

 const useKeyPress = targetKey => {
-  const [keyPressed, setKeyPressed] = React.useState(false);
+  const [keyPressed, setKeyPressed] = useState(false);
 
   const downHandler = ({ key }) => {
-    if (key === targetKey) setKeyPressed(true);
+    if (key === targetKey) {
+      setKeyPressed(true);
+    }
   };
 
   const upHandler = ({ key }) => {
-    if (key === targetKey) setKeyPressed(false);
+    if (key === targetKey) {
+      setKeyPressed(false);
+    }
   };
 
-  React.useEffect(() => {
-    window.addEventListener('keydown', downHandler);
-    window.addEventListener('keyup', upHandler);
-
-    return () => {
-      window.removeEventListener('keydown', downHandler);
-      window.removeEventListener('keyup', upHandler);
-    };
-  }, []);
-
-  return keyPressed;
-};
+  useEffect(() => {
```

### CountDown (task/30)

#### canonical solution

```javascript
const CountDown = ({ hours = 0, minutes = 0, seconds = 0 }) => {
  const [paused, setPaused] = React.useState(false);
  const [over, setOver] = React.useState(false);
  const [[h, m, s], setTime] = React.useState([hours, minutes, seconds]);

  const tick = () => {
    if (paused || over) return;
    if (h === 0 && m === 0 && s === 0) setOver(true);
    else if (m === 0 && s === 0) {
      setTime([h - 1, 59, 59]);
    } else if (s == 0) {
      setTime([h, m - 1, 59]);
    } else {
      setTime([h, m, s - 1]);
    }
  };

  const reset = () => {
    setTime([parseInt(hours), parseInt(minutes), parseInt(seconds)]);
    setPaused(false);
    setOver(false);
  };

  React.useEffect(() => {
    const timerID = setInterval(() => tick(), 1000);
    return () => clearInterval(timerID);
  });

  return (
    <div>
      <p>{`${h.toString().padStart(2, '0')}:${m
        .toString()
        .padStart(2, '0')}:${s.toString().padStart(2, '0')}`}</p>
      <div>{over ? "Time's up!" : ''}</div>
      <button onClick={() => setPaused(!paused)}>
        {paused ? 'Resume' : 'Pause'}
      </button>
      <button onClick={() => reset()}>Restart</button>
    </div>
  );
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,41 +1,9 @@

 const CountDown = ({ hours = 0, minutes = 0, seconds = 0 }) => {
-  const [paused, setPaused] = React.useState(false);
-  const [over, setOver] = React.useState(false);
-  const [[h, m, s], setTime] = React.useState([hours, minutes, seconds]);
+  const [countDown, setCountDown] = useState({ hours, minutes, seconds });
+  const [timeOut, setTimeOut] = useState(false);
 
-  const tick = () => {
-    if (paused || over) return;
-    if (h === 0 && m === 0 && s === 0) setOver(true);
-    else if (m === 0 && s === 0) {
-      setTime([h - 1, 59, 59]);
-    } else if (s == 0) {
-      setTime([h, m - 1, 59]);
-    } else {
-      setTime([h, m, s - 1]);
-    }
-  };
-
-  const reset = () => {
-    setTime([parseInt(hours), parseInt(minutes), parseInt(seconds)]);
-    setPaused(false);
-    setOver(false);
-  };
-
-  React.useEffect(() => {
-    const timerID = setInterval(() => tick(), 1000);
-    return () => clearInterval(timerID);
-  });
-
-  return (
-    <div>
-      <p>{`${h.toString().padStart(2, '0')}:${m
-        .toString()
-        .padStart(2, '0')}:${s.toString().padStart(2, '0')}`}</p>
-      <div>{over ? "Time's up!" : ''}</div>
-      <button onClick={() => setPaused(!paused)}>
-        {paused ? 'Resume' : 'Pause'}
-      </button>
-      <button onClick={() => reset()}>Restart</button>
-    </div>
-  );
-};
+  useEffect(() => {
+    if (hours > 0 || minutes > 0 || seconds > 0) {
+      let interval = setInterval(() => {
+        setCountDown(prevCountDown => {
+          const newCountDown = { ...prevCountDown };
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,41 +1,13 @@

 const CountDown = ({ hours = 0, minutes = 0, seconds = 0 }) => {
-  const [paused, setPaused] = React.useState(false);
-  const [over, setOver] = React.useState(false);
-  const [[h, m, s], setTime] = React.useState([hours, minutes, seconds]);
+  const [timeLeft, setTimeLeft] = useState(0);
 
-  const tick = () => {
-    if (paused || over) return;
-    if (h === 0 && m === 0 && s === 0) setOver(true);
-    else if (m === 0 && s === 0) {
-      setTime([h - 1, 59, 59]);
-    } else if (s == 0) {
-      setTime([h, m - 1, 59]);
-    } else {
-      setTime([h, m, s - 1]);
-    }
-  };
+  useEffect(() => {
+    setTimeLeft(hours * 3600 + minutes * 60 + seconds);
+  }, [hours, minutes, seconds]);
 
-  const reset = () => {
-    setTime([parseInt(hours), parseInt(minutes), parseInt(seconds)]);
-    setPaused(false);
-    setOver(false);
-  };
+  useEffect(() => {
+    const timerId = setInterval(() => {
+      setTimeLeft(t => t - 1);
+    }, 1000);
 
-  React.useEffect(() => {
-    const timerID = setInterval(() => tick(), 1000);
-    return () => clearInterval(timerID);
-  });
-
-  return (
-    <div>
-      <p>{`${h.toString().padStart(2, '0')}:${m
-        .toString()
-        .padStart(2, '0')}:${s.toString().padStart(2, '0')}`}</p>
-      <div>{over ? "Time's up!" : ''}</div>
-      <button onClick={() => setPaused(!paused)}>
-        {paused ? 'Resume' : 'Pause'}
-      </button>
-      <button onClick={() => reset()}>Restart</button>
-    </div>
-  );
-};
+    return () => clearInterval(
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,41 +1,9 @@

 const CountDown = ({ hours = 0, minutes = 0, seconds = 0 }) => {
-  const [paused, setPaused] = React.useState(false);
-  const [over, setOver] = React.useState(false);
-  const [[h, m, s], setTime] = React.useState([hours, minutes, seconds]);
-
-  const tick = () => {
-    if (paused || over) return;
-    if (h === 0 && m === 0 && s === 0) setOver(true);
-    else if (m === 0 && s === 0) {
-      setTime([h - 1, 59, 59]);
-    } else if (s == 0) {
-      setTime([h, m - 1, 59]);
-    } else {
-      setTime([h, m, s - 1]);
-    }
-  };
-
-  const reset = () => {
-    setTime([parseInt(hours), parseInt(minutes), parseInt(seconds)]);
-    setPaused(false);
-    setOver(false);
-  };
-
-  React.useEffect(() => {
-    const timerID = setInterval(() => tick(), 1000);
-    return () => clearInterval(timerID);
-  });
-
   return (
-    <div>
-      <p>{`${h.toString().padStart(2, '0')}:${m
-        .toString()
-        .padStart(2, '0')}:${s.toString().padStart(2, '0')}`}</p>
-      <div>{over ? "Time's up!" : ''}</div>
-      <button onClick={() => setPaused(!paused)}>
-        {paused ? 'Resume' : 'Pause'}
-      </button>
-      <button onClick={() => reset()}>Restart</button>
-    </div>
-  );
-};
+    <div className="countdown-container">
+      <div className="countdown-item">
+        <span className="countdown-value">{hours}</span>
+        <span className="countdown-label">Hours</span>
+      </div>
+      <div className="countdown-item">
+        <span className="countdown-value">{minutes}</span>
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,41 +1,14 @@

 const CountDown = ({ hours = 0, minutes = 0, seconds = 0 }) => {
-  const [paused, setPaused] = React.useState(false);
-  const [over, setOver] = React.useState(false);
-  const [[h, m, s], setTime] = React.useState([hours, minutes, seconds]);
+  const [timeLeft, setTimeLeft] = useState(
+    (hours * 3600) + (minutes * 60) + seconds
+  );
 
-  const tick = () => {
-    if (paused || over) return;
-    if (h === 0 && m === 0 && s === 0) setOver(true);
-    else if (m === 0 && s === 0) {
-      setTime([h - 1, 59, 59]);
-    } else if (s == 0) {
-      setTime([h, m - 1, 59]);
-    } else {
-      setTime([h, m, s - 1]);
-    }
-  };
+  useEffect(() => {
+    const timer = setInterval(() => {
+      setTimeLeft(timeLeft - 1);
+    }, 1000);
 
-  const reset = () => {
-    setTime([parseInt(hours), parseInt(minutes), parseInt(seconds)]);
-    setPaused(false);
-    setOver(false);
-  };
+    return () => clearInterval(timer);
+  }, [timeLeft]);
 
-  React.useEffect(() => {
-    const timerID = setInterval(() => tick(), 1000);
-    return () => clearInterval(timerID);
-  });
-
-  return (
-    <div>
-      <p>{`${h.toString().padStart(2, '0')}:${m
-        .toString()
-        .padStart(2, '0')}:${s.toString().padStart(2, '0')}`}</p>
-      <div>{over ? "Time's up!" : ''}</div>
-      <button onClick={() => setPaused(!paused)}>
-        {paused ? 'Resume' : 'Pause'}
-      </button>
-      <button onClick={() => reset()}>Restart</button>
-    </div>
-  );
-};
+  const time = timeLeft => {
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,41 +1,9 @@

 const CountDown = ({ hours = 0, minutes = 0, seconds = 0 }) => {
-  const [paused, setPaused] = React.useState(false);
-  const [over, setOver] = React.useState(false);
-  const [[h, m, s], setTime] = React.useState([hours, minutes, seconds]);
-
-  const tick = () => {
-    if (paused || over) return;
-    if (h === 0 && m === 0 && s === 0) setOver(true);
-    else if (m === 0 && s === 0) {
-      setTime([h - 1, 59, 59]);
-    } else if (s == 0) {
-      setTime([h, m - 1, 59]);
-    } else {
-      setTime([h, m, s - 1]);
-    }
-  };
-
-  const reset = () => {
-    setTime([parseInt(hours), parseInt(minutes), parseInt(seconds)]);
-    setPaused(false);
-    setOver(false);
-  };
-
-  React.useEffect(() => {
-    const timerID = setInterval(() => tick(), 1000);
-    return () => clearInterval(timerID);
-  });
-
   return (
-    <div>
-      <p>{`${h.toString().padStart(2, '0')}:${m
-        .toString()
-        .padStart(2, '0')}:${s.toString().padStart(2, '0')}`}</p>
-      <div>{over ? "Time's up!" : ''}</div>
-      <button onClick={() => setPaused(!paused)}>
-        {paused ? 'Resume' : 'Pause'}
-      </button>
-      <button onClick={() => reset()}>Restart</button>
+    <div className="CountDown">
+      <div className="CountDown__days">{`${hours} : ${minutes} : ${seconds}`}</div>
     </div>
   );
 };
+
+export default CountDown;
```

### Alert (task/31)

#### canonical solution

```javascript
const Alert = ({ isDefaultShown = false, timeout = 250, type, message }) => {
  const [isShown, setIsShown] = React.useState(isDefaultShown);
  const [isLeaving, setIsLeaving] = React.useState(false);

  let timeoutId = null;

  React.useEffect(() => {
    setIsShown(true);
    return () => {
      clearTimeout(timeoutId);
    };
  }, [isDefaultShown, timeout, timeoutId]);

  const closeAlert = () => {
    setIsLeaving(true);
    timeoutId = setTimeout(() => {
      setIsLeaving(false);
      setIsShown(false);
    }, timeout);
  };

  return (
    isShown && (
      <div
        className={`alert ${type} ${isLeaving ? 'leaving' : ''}`}
        role="alert"
      >
        <button className="close" onClick={closeAlert} />
        {message}
      </div>
    )
  );
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,33 +1,15 @@

 const Alert = ({ isDefaultShown = false, timeout = 250, type, message }) => {
-  const [isShown, setIsShown] = React.useState(isDefaultShown);
-  const [isLeaving, setIsLeaving] = React.useState(false);
+  const [isShown, setIsShown] = useState(isDefaultShown);
+  const classes = useStyles();
 
-  let timeoutId = null;
-
-  React.useEffect(() => {
-    setIsShown(true);
-    return () => {
-      clearTimeout(timeoutId);
-    };
-  }, [isDefaultShown, timeout, timeoutId]);
-
-  const closeAlert = () => {
-    setIsLeaving(true);
-    timeoutId = setTimeout(() => {
-      setIsLeaving(false);
-      setIsShown(false);
-    }, timeout);
-  };
+  useEffect(() => {
+    if (isDefaultShown) {
+      setTimeout(() => {
+        setIsShown(false);
+      }, timeout);
+    }
+  }, [isDefaultShown, timeout]);
 
   return (
-    isShown && (
-      <div
-        className={`alert ${type} ${isLeaving ? 'leaving' : ''}`}
-        role="alert"
-      >
-        <button className="close" onClick={closeAlert} />
-        {message}
-      </div>
-    )
-  );
-};
+    <Snackbar
+      classes=
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,33 +1,10 @@

 const Alert = ({ isDefaultShown = false, timeout = 250, type, message }) => {
-  const [isShown, setIsShown] = React.useState(isDefaultShown);
-  const [isLeaving, setIsLeaving] = React.useState(false);
+  const [isShown, setIsShown] = useState(isDefaultShown);
+  const [startTime, setStartTime] = useState(Date.now());
+  const [transitionTime, setTransitionTime] = useState(0);
 
-  let timeoutId = null;
-
-  React.useEffect(() => {
-    setIsShown(true);
-    return () => {
-      clearTimeout(timeoutId);
-    };
-  }, [isDefaultShown, timeout, timeoutId]);
-
-  const closeAlert = () => {
-    setIsLeaving(true);
-    timeoutId = setTimeout(() => {
-      setIsLeaving(false);
-      setIsShown(false);
-    }, timeout);
-  };
-
-  return (
-    isShown && (
-      <div
-        className={`alert ${type} ${isLeaving ? 'leaving' : ''}`}
-        role="alert"
-      >
-        <button className="close" onClick={closeAlert} />
-        {message}
-      </div>
-    )
-  );
-};
+  useEffect(() => {
+    if (isDefaultShown) {
+      setIsShown(true);
+      setStartTime(Date.now());
+     
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,33 +1,13 @@

 const Alert = ({ isDefaultShown = false, timeout = 250, type, message }) => {
-  const [isShown, setIsShown] = React.useState(isDefaultShown);
-  const [isLeaving, setIsLeaving] = React.useState(false);
+  const [isAlertShown, setIsAlertShown] = useState(isDefaultShown);
+  const [isClosing, setIsClosing] = useState(false);
 
-  let timeoutId = null;
-
-  React.useEffect(() => {
-    setIsShown(true);
-    return () => {
-      clearTimeout(timeoutId);
-    };
-  }, [isDefaultShown, timeout, timeoutId]);
-
-  const closeAlert = () => {
-    setIsLeaving(true);
-    timeoutId = setTimeout(() => {
-      setIsLeaving(false);
-      setIsShown(false);
+  const onClose = () => {
+    setIsAlertShown(false);
+    setIsClosing(true);
+    setTimeout(() => {
+      setIsClosing(false);
     }, timeout);
   };
 
-  return (
-    isShown && (
-      <div
-        className={`alert ${type} ${isLeaving ? 'leaving' : ''}`}
-        role="alert"
-      >
-        <button className="close" onClick={closeAlert} />
-        {message}
-      </div>
-    )
-  );
-};
+  use
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,33 +1,14 @@

 const Alert = ({ isDefaultShown = false, timeout = 250, type, message }) => {
-  const [isShown, setIsShown] = React.useState(isDefaultShown);
-  const [isLeaving, setIsLeaving] = React.useState(false);
+  const [show, setShow] = useState(isDefaultShown);
+  const [isClosing, setIsClosing] = useState(false);
 
-  let timeoutId = null;
-
-  React.useEffect(() => {
-    setIsShown(true);
-    return () => {
-      clearTimeout(timeoutId);
-    };
-  }, [isDefaultShown, timeout, timeoutId]);
-
-  const closeAlert = () => {
-    setIsLeaving(true);
-    timeoutId = setTimeout(() => {
-      setIsLeaving(false);
-      setIsShown(false);
+  const handleClose = () => {
+    setIsClosing(true);
+    setTimeout(() => {
+      setShow(false);
+      setIsClosing(false);
     }, timeout);
   };
 
-  return (
-    isShown && (
-      <div
-        className={`alert ${type} ${isLeaving ? 'leaving' : ''}`}
-        role="alert"
-      >
-        <button className="close" onClick={closeAlert} />
-        {message}
-      </div>
-    )
-  );
-};
+  const closeAlert = () => {
+    set
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,33 +1,14 @@

 const Alert = ({ isDefaultShown = false, timeout = 250, type, message }) => {
-  const [isShown, setIsShown] = React.useState(isDefaultShown);
-  const [isLeaving, setIsLeaving] = React.useState(false);
+  const [visible, setVisible] = useState(isDefaultShown);
+  const [timer, setTimer] = useState(null);
 
-  let timeoutId = null;
-
-  React.useEffect(() => {
-    setIsShown(true);
-    return () => {
-      clearTimeout(timeoutId);
-    };
-  }, [isDefaultShown, timeout, timeoutId]);
-
-  const closeAlert = () => {
-    setIsLeaving(true);
-    timeoutId = setTimeout(() => {
-      setIsLeaving(false);
-      setIsShown(false);
-    }, timeout);
+  const handleClose = () => {
+    setVisible(false);
+    setTimer(null);
   };
 
-  return (
-    isShown && (
-      <div
-        className={`alert ${type} ${isLeaving ? 'leaving' : ''}`}
-        role="alert"
-      >
-        <button className="close" onClick={closeAlert} />
-        {message}
-      </div>
-    )
-  );
-};
+  useEffect(() => {
+    if (isDefaultShown) {
+      setVisible(true);
+      setTimer(
+        setTimeout(() =>
```

### useHash (task/32)

#### canonical solution

```javascript
const useHash = () => {
  const [hash, setHash] = React.useState(() => window.location.hash);

  const hashChangeHandler = React.useCallback(() => {
    setHash(window.location.hash);
  }, []);

  React.useEffect(() => {
    window.addEventListener('hashchange', hashChangeHandler);
    return () => {
      window.removeEventListener('hashchange', hashChangeHandler);
    };
  }, []);

  const updateHash = React.useCallback(
    newHash => {
      if (newHash !== hash) window.location.hash = newHash;
    },
    [hash]
  );

  return [hash, updateHash];
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,23 +1,11 @@

 const useHash = () => {
-  const [hash, setHash] = React.useState(() => window.location.hash);
+  return window.location.hash.split('#')[1];
+};
 
-  const hashChangeHandler = React.useCallback(() => {
-    setHash(window.location.hash);
-  }, []);
+const useQuery = () => {
+  return window.location.search.split('?')[1];
+};
 
-  React.useEffect(() => {
-    window.addEventListener('hashchange', hashChangeHandler);
-    return () => {
-      window.removeEventListener('hashchange', hashChangeHandler);
-    };
-  }, []);
-
-  const updateHash = React.useCallback(
-    newHash => {
-      if (newHash !== hash) window.location.hash = newHash;
-    },
-    [hash]
-  );
-
-  return [hash, updateHash];
-};
+const appendToURL = (query, hash) => {
+  const newURL = `${window.location.origin}${window.location.pathname}?${query}#${hash}`;
+  window.history.pushState({
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,23 +1,12 @@

 const useHash = () => {
-  const [hash, setHash] = React.useState(() => window.location.hash);
+  const [path, setPath] = useState('');
+  const location = useLocation();
 
-  const hashChangeHandler = React.useCallback(() => {
-    setHash(window.location.hash);
-  }, []);
+  useEffect(() => {
+    setPath(location.hash.slice(1));
+  }, [location]);
 
-  React.useEffect(() => {
-    window.addEventListener('hashchange', hashChangeHandler);
-    return () => {
-      window.removeEventListener('hashchange', hashChangeHandler);
-    };
-  }, []);
+  return path;
+};
 
-  const updateHash = React.useCallback(
-    newHash => {
-      if (newHash !== hash) window.location.hash = newHash;
-    },
-    [hash]
-  );
-
-  return [hash, updateHash];
-};
+export default useHash;
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,23 +1,14 @@

 const useHash = () => {
-  const [hash, setHash] = React.useState(() => window.location.hash);
+  const [href, setHref] = useState(location.href);
+  const [hash, setHash] = useState(location.hash);
 
-  const hashChangeHandler = React.useCallback(() => {
-    setHash(window.location.hash);
-  }, []);
+  useEffect(() => {
+    const handlePopState = () => {
+      setHref(location.href);
+      setHash(location.hash);
+    };
 
-  React.useEffect(() => {
-    window.addEventListener('hashchange', hashChangeHandler);
+    window.addEventListener('popstate', handlePopState);
+
     return () => {
-      window.removeEventListener('hashchange', hashChangeHandler);
-    };
-  }, []);
-
-  const updateHash = React.useCallback(
-    newHash => {
-      if (newHash !== hash) window.location.hash = newHash;
-    },
-    [hash]
-  );
-
-  return [hash, updateHash];
-};
+      window
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,23 +1,5 @@

 const useHash = () => {
-  const [hash, setHash] = React.useState(() => window.location.hash);
+  return useMountedState().hash;
+};
 
-  const hashChangeHandler = React.useCallback(() => {
-    setHash(window.location.hash);
-  }, []);
-
-  React.useEffect(() => {
-    window.addEventListener('hashchange', hashChangeHandler);
-    return () => {
-      window.removeEventListener('hashchange', hashChangeHandler);
-    };
-  }, []);
-
-  const updateHash = React.useCallback(
-    newHash => {
-      if (newHash !== hash) window.location.hash = newHash;
-    },
-    [hash]
-  );
-
-  return [hash, updateHash];
-};
+export default useHash;
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,23 +1,13 @@

 const useHash = () => {
-  const [hash, setHash] = React.useState(() => window.location.hash);
-
-  const hashChangeHandler = React.useCallback(() => {
-    setHash(window.location.hash);
-  }, []);
-
-  React.useEffect(() => {
-    window.addEventListener('hashchange', hashChangeHandler);
+  const [hash, setHash] = useState(window.location.hash);
+  useEffect(() => {
+    window.addEventListener('hashchange', () => {
+      setHash(window.location.hash);
+    });
     return () => {
-      window.removeEventListener('hashchange', hashChangeHandler);
+      window.removeEventListener('hashchange', () => {
+        setHash(window.location.hash);
+      });
     };
   }, []);
-
-  const updateHash = React.useCallback(
-    newHash => {
-      if (newHash !== hash) window.location.hash = newHash;
-    },
-    [hash]
-  );
-
-  return [hash, updateHash];
-};
+ 
```

### useDelayedState (task/33)

#### canonical solution

```javascript
const useDelayedState = (initialState, condition) => {
  const [{ state, loaded }, setState] = React.useState({
    state: null,
    loaded: false,
  });

  React.useEffect(() => {
    if (!loaded && condition) setState({ state: initialState, loaded: true });
  }, [condition, loaded]);

  const updateState = newState => {
    if (!loaded) return;
    setState({ state: newState, loaded });
  };

  return [state, updateState];
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,17 +1,13 @@

 const useDelayedState = (initialState, condition) => {
-  const [{ state, loaded }, setState] = React.useState({
-    state: null,
-    loaded: false,
-  });
+  const [value, setValue] = useState(initialState);
+  const [delayedValue, setDelayedValue] = useState(initialState);
 
-  React.useEffect(() => {
-    if (!loaded && condition) setState({ state: initialState, loaded: true });
-  }, [condition, loaded]);
+  useEffect(() => {
+    if (condition(value)) {
+      setDelayedValue(value);
+    }
+  }, [value]);
 
-  const updateState = newState => {
-    if (!loaded) return;
-    setState({ state: newState, loaded });
-  };
-
-  return [state, updateState];
-};
+  useEffect(() => {
+    if (condition(delayedValue)) {
+      setValue(delayedValue);
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,17 +1,15 @@

 const useDelayedState = (initialState, condition) => {
-  const [{ state, loaded }, setState] = React.useState({
-    state: null,
-    loaded: false,
-  });
+  const [state, setState] = useState(initialState);
+  const [isTrue, setIsTrue] = useState(false);
 
-  React.useEffect(() => {
-    if (!loaded && condition) setState({ state: initialState, loaded: true });
-  }, [condition, loaded]);
+  useEffect(() => {
+    if (condition) {
+      setIsTrue(true);
+    }
+  }, [condition]);
 
-  const updateState = newState => {
-    if (!loaded) return;
-    setState({ state: newState, loaded });
-  };
-
-  return [state, updateState];
-};
+  useEffect(() => {
+    if (isTrue) {
+      setState(initialState);
+      setIsTrue(false);
+   
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,17 +1,15 @@

 const useDelayedState = (initialState, condition) => {
-  const [{ state, loaded }, setState] = React.useState({
-    state: null,
-    loaded: false,
-  });
+  const [state, setState] = useState(initialState);
+  const [delayedState, setDelayedState] = useState(initialState);
 
-  React.useEffect(() => {
-    if (!loaded && condition) setState({ state: initialState, loaded: true });
-  }, [condition, loaded]);
+  useEffect(() => {
+    if (condition) {
+      setDelayedState(state);
+    }
+  }, [state, condition]);
 
-  const updateState = newState => {
-    if (!loaded) return;
-    setState({ state: newState, loaded });
-  };
+  useEffect(() => {
+    setState(delayedState);
+  }, [delayedState]);
 
-  return [state, updateState];
-};
+  return
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,17 +1,14 @@

 const useDelayedState = (initialState, condition) => {
-  const [{ state, loaded }, setState] = React.useState({
-    state: null,
-    loaded: false,
-  });
+  const [delayedState, setDelayedState] = useState(initialState);
+  const [delayed, setDelayed] = useState(false);
 
-  React.useEffect(() => {
-    if (!loaded && condition) setState({ state: initialState, loaded: true });
-  }, [condition, loaded]);
+  useEffect(() => {
+    if (condition) {
+      setDelayed(true);
+    }
+  }, [condition]);
 
-  const updateState = newState => {
-    if (!loaded) return;
-    setState({ state: newState, loaded });
-  };
-
-  return [state, updateState];
-};
+  useEffect(() => {
+    if (delayed) {
+      setDelayedState(initialState);
+    }
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,17 +1,13 @@

 const useDelayedState = (initialState, condition) => {
-  const [{ state, loaded }, setState] = React.useState({
-    state: null,
-    loaded: false,
-  });
+  const [delayedState, setDelayedState] = useState(initialState);
+  const [delayTimer, setDelayTimer] = useState(null);
 
-  React.useEffect(() => {
-    if (!loaded && condition) setState({ state: initialState, loaded: true });
-  }, [condition, loaded]);
+  useEffect(() => {
+    return () => {
+      clearTimeout(delayTimer);
+    };
+  }, [delayTimer]);
 
-  const updateState = newState => {
-    if (!loaded) return;
-    setState({ state: newState, loaded });
-  };
-
-  return [state, updateState];
-};
+  const onChange = (value) => {
+    clearTimeout(delayTimer);
+    setDelayedState(value);
```

### useSearchParam (task/34)

#### canonical solution

```javascript
const useSearchParam = param => {
  const getValue = React.useCallback(
    () => new URLSearchParams(window.location.search).get(param),
    [param]
  );

  const [value, setValue] = React.useState(getValue);

  React.useEffect(() => {
    const onChange = () => {
      setValue(getValue());
    };

    window.addEventListener('popstate', onChange);
    window.addEventListener('pushstate', onChange);
    window.addEventListener('replacestate', onChange);

    return () => {
      window.removeEventListener('popstate', onChange);
      window.removeEventListener('pushstate', onChange);
      window.removeEventListener('replacestate', onChange);
    };
  }, []);

  return value;
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,26 +1,10 @@

 const useSearchParam = param => {
-  const getValue = React.useCallback(
-    () => new URLSearchParams(window.location.search).get(param),
-    [param]
-  );
+	const [value, setValue] = useState(getSearchParam(param) || '');
+	const onChange = event => {
+		setValue(event.target.value);
+		setSearchParam(param, event.target.value);
+	};
+	return [value, onChange];
+};
 
-  const [value, setValue] = React.useState(getValue);
-
-  React.useEffect(() => {
-    const onChange = () => {
-      setValue(getValue());
-    };
-
-    window.addEventListener('popstate', onChange);
-    window.addEventListener('pushstate', onChange);
-    window.addEventListener('replacestate', onChange);
-
-    return () => {
-      window.removeEventListener('popstate', onChange);
-      window.removeEventListener('pushstate', onChange);
-      window.removeEventListener('replacestate', onChange);
-    };
-  }, []);
-
-  return value;
-};
+export default useSearchParam;
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,26 +1,10 @@

 const useSearchParam = param => {
-  const getValue = React.useCallback(
-    () => new URLSearchParams(window.location.search).get(param),
-    [param]
-  );
+    const [query, setQuery] = useState(param || "");
+    const [results, setResults] = useState([]);
+    const [isFetching, setIsFetching] = useState(false);
 
-  const [value, setValue] = React.useState(getValue);
-
-  React.useEffect(() => {
-    const onChange = () => {
-      setValue(getValue());
-    };
-
-    window.addEventListener('popstate', onChange);
-    window.addEventListener('pushstate', onChange);
-    window.addEventListener('replacestate', onChange);
-
-    return () => {
-      window.removeEventListener('popstate', onChange);
-      window.removeEventListener('pushstate', onChange);
-      window.removeEventListener('replacestate', onChange);
-    };
-  }, []);
-
-  return value;
-};
+    const search = useCallback(async query => {
+        setIsFetching(true);
+        setResults([]);
+        const { results } = await getUsers(query);
+        set
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,26 +1,10 @@

 const useSearchParam = param => {
-  const getValue = React.useCallback(
-    () => new URLSearchParams(window.location.search).get(param),
-    [param]
-  );
+  const [value, setValue] = useState('');
+  const [query, setQuery] = useState(window.location.search);
 
-  const [value, setValue] = React.useState(getValue);
-
-  React.useEffect(() => {
-    const onChange = () => {
-      setValue(getValue());
-    };
-
-    window.addEventListener('popstate', onChange);
-    window.addEventListener('pushstate', onChange);
-    window.addEventListener('replacestate', onChange);
-
-    return () => {
-      window.removeEventListener('popstate', onChange);
-      window.removeEventListener('pushstate', onChange);
-      window.removeEventListener('replacestate', onChange);
-    };
-  }, []);
-
-  return value;
-};
+  useEffect(() => {
+    if (query) {
+      const q = query.slice(1).split('&');
+      const queryObj = q.reduce((a, b) => {
+        const c = b.split('=');
+        a[c[0
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,26 +1,11 @@

 const useSearchParam = param => {
-  const getValue = React.useCallback(
-    () => new URLSearchParams(window.location.search).get(param),
-    [param]
-  );
+  const [paramValue, setParamValue] = useState('');
+  const [searchValue, setSearchValue] = useState('');
 
-  const [value, setValue] = React.useState(getValue);
-
-  React.useEffect(() => {
-    const onChange = () => {
-      setValue(getValue());
-    };
-
-    window.addEventListener('popstate', onChange);
-    window.addEventListener('pushstate', onChange);
-    window.addEventListener('replacestate', onChange);
-
-    return () => {
-      window.removeEventListener('popstate', onChange);
-      window.removeEventListener('pushstate', onChange);
-      window.removeEventListener('replacestate', onChange);
-    };
-  }, []);
-
-  return value;
-};
+  const handleSearchValue = e => {
+    const value = e.target.value;
+    setSearchValue(value);
+    if (param === 'keyword') {
+      searchByKeyword(value);
+    } else if (param === 'tags') {
+      searchBy
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,26 +1,9 @@

 const useSearchParam = param => {
-  const getValue = React.useCallback(
-    () => new URLSearchParams(window.location.search).get(param),
-    [param]
-  );
+  const [value, setValue] = useState('');
+  const [state, setState] = useState({});
 
-  const [value, setValue] = React.useState(getValue);
-
-  React.useEffect(() => {
-    const onChange = () => {
-      setValue(getValue());
-    };
-
-    window.addEventListener('popstate', onChange);
-    window.addEventListener('pushstate', onChange);
-    window.addEventListener('replacestate', onChange);
-
-    return () => {
-      window.removeEventListener('popstate', onChange);
-      window.removeEventListener('pushstate', onChange);
-      window.removeEventListener('replacestate', onChange);
-    };
-  }, []);
-
-  return value;
-};
+  const [getParam, setParam] = useState(() => {
+    const rawParam = window.location.search;
+    if (rawParam) {
+      const queryString = decodeURIComponent(rawParam);
+      const query = queryString.substring(1).split('&');
```

### useUpdate (task/35)

#### canonical solution

```javascript
const useUpdate = () => {
  const [, update] = React.useReducer(() => ({}));
  return update;
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,4 +1,9 @@

 const useUpdate = () => {
-  const [, update] = React.useReducer(() => ({}));
-  return update;
-};
+  const [update, { loading, error }] = useMutation(Mutation.UPDATE_USER);
+  const updateHandler = useCallback(
+    (values: FormData) => {
+      update({
+        variables: {
+          input: {
+            id: values.id,
+            name: values.name,
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,4 +1,6 @@

 const useUpdate = () => {
-  const [, update] = React.useReducer(() => ({}));
+  const [, update] = useReducer(reducer, initialState);
   return update;
 };
+
+export default useUpdate;
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,4 +1,9 @@

 const useUpdate = () => {
-  const [, update] = React.useReducer(() => ({}));
-  return update;
+  const [, forceUpdate] = useState(0);
+  return () => forceUpdate(Math.random());
 };
+
+const useUpdate2 = () => {
+  const [, forceUpdate] = useState(0);
+  return () => forceUpdate(Math.random());
+};
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,4 +1,8 @@

 const useUpdate = () => {
-  const [, update] = React.useReducer(() => ({}));
-  return update;
-};
+  const [isLoading, setIsLoading] = useState(false);
+  const [isSuccess, setIsSuccess] = useState(false);
+  const [isError, setIsError] = useState(false);
+  const [user, setUser] = useState(null);
+
+  const updateUser = async (userId, firstName, lastName, phone, imageUrl) => {
+    setIsLoading(true);
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,4 +1,9 @@

 const useUpdate = () => {
-  const [, update] = React.useReducer(() => ({}));
-  return update;
-};
+    const state = useRef({
+        selected: 0,
+        data: []
+    })
+    const {selected, data} = state.current
+
+    const [onUpdate, setData] = useState(() => {
+        return {
```

### Select (task/36)

#### canonical solution

```javascript
const Select = ({ values, onValueChange, selectedValue, ...rest }) => {
  return (
    <select
      defaultValue={selectedValue}
      onChange={({ target: { value } }) => onValueChange(value)}
      {...rest}
    >
      {values.map(([value, text]) => (
        <option key={value} value={value}>
          {text}
        </option>
      ))}
    </select>
  );
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,15 +1,17 @@

 const Select = ({ values, onValueChange, selectedValue, ...rest }) => {
+  const selectValue = v => {
+    onValueChange(v);
+  };
+
   return (
-    <select
-      defaultValue={selectedValue}
-      onChange={({ target: { value } }) => onValueChange(value)}
-      {...rest}
-    >
-      {values.map(([value, text]) => (
-        <option key={value} value={value}>
-          {text}
-        </option>
+    <StyledSelect {...rest}>
+      {values.map(({ label, value }) => (
+        <Option
+          key={value}
+          onClick={() => selectValue(value)}
+          disabled={value === selectedValue}
+        >
+          {label}
+        </Option>
       ))}
-    </select>
-  );
-};
+   
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,15 +1,14 @@

 const Select = ({ values, onValueChange, selectedValue, ...rest }) => {
+  const handleChange = (e) => {
+    const { value } = e.target;
+    onValueChange(value);
+  };
+
   return (
-    <select
-      defaultValue={selectedValue}
-      onChange={({ target: { value } }) => onValueChange(value)}
-      {...rest}
-    >
-      {values.map(([value, text]) => (
+    <select {...rest} value={selectedValue} onChange={handleChange}>
+      {values.map((value) => (
         <option key={value} value={value}>
-          {text}
+          {value}
         </option>
       ))}
-    </select>
-  );
-};
+    </select
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,15 +1,14 @@

 const Select = ({ values, onValueChange, selectedValue, ...rest }) => {
+  const handleOnChange = (e) => {
+    onValueChange(e.target.value);
+  };
+
   return (
-    <select
-      defaultValue={selectedValue}
-      onChange={({ target: { value } }) => onValueChange(value)}
-      {...rest}
-    >
-      {values.map(([value, text]) => (
+    <select {...rest} value={selectedValue} onChange={handleOnChange}>
+      {values.map((value) => (
         <option key={value} value={value}>
-          {text}
+          {value}
         </option>
       ))}
     </select>
   );
-};
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,15 +1,15 @@

 const Select = ({ values, onValueChange, selectedValue, ...rest }) => {
-  return (
-    <select
-      defaultValue={selectedValue}
-      onChange={({ target: { value } }) => onValueChange(value)}
-      {...rest}
-    >
-      {values.map(([value, text]) => (
-        <option key={value} value={value}>
-          {text}
-        </option>
-      ))}
-    </select>
-  );
-};
+  const [ menuOpen, setMenuOpen ] = useState(false);
+  const [ menuHeight, setMenuHeight ] = useState(0);
+  const ref = useRef(null);
+
+  const handleValueChange = (option) => {
+    onValueChange(option);
+    setMenuOpen(false);
+  };
+
+  const handleBlur = () => {
+    setMenuOpen(false);
+  };
+
+  const
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,15 +1,20 @@

 const Select = ({ values, onValueChange, selectedValue, ...rest }) => {
+  const options = values.map(value => (
+    <option key={value} value={value}>
+      {value}
+    </option>
+  ));
+
   return (
     <select
-      defaultValue={selectedValue}
-      onChange={({ target: { value } }) => onValueChange(value)}
       {...rest}
+      onChange={onValueChange}
+      value={selectedValue}
+      data-testid="select"
     >
-      {values.map(([value, text]) => (
-        <option key={value} value={value}>
-          {text}
-        </option>
-      ))}
+      {options}
     </select>
   );
 };
+
+Select.
```

### LimitedWordTextarea (task/37)

#### canonical solution

```javascript
const LimitedWordTextarea = ({ rows, cols, value, limit }) => {
  const [{ content, wordCount }, setContent] = React.useState({
    content: value,
    wordCount: 0
  });

  const setFormattedContent = React.useCallback(
    text => {
      let words = text.split(' ').filter(Boolean);
      if (words.length > limit) {
        setContent({
          content: words.slice(0, limit).join(' '),
          wordCount: limit
        });
      } else {
        setContent({ content: text, wordCount: words.length });
      }
    },
    [limit, setContent]
  );

  React.useEffect(() => {
    setFormattedContent(content);
  }, []);

  return (
    <>
      <textarea
        rows={rows}
        cols={cols}
        onChange={event => setFormattedContent(event.target.value)}
        value={content}
      />
      <p>
        {wordCount}/{limit}
      </p>
    </>
  );
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,39 +1,16 @@

 const LimitedWordTextarea = ({ rows, cols, value, limit }) => {
-  const [{ content, wordCount }, setContent] = React.useState({
-    content: value,
-    wordCount: 0
-  });
-
-  const setFormattedContent = React.useCallback(
-    text => {
-      let words = text.split(' ').filter(Boolean);
-      if (words.length > limit) {
-        setContent({
-          content: words.slice(0, limit).join(' '),
-          wordCount: limit
-        });
-      } else {
-        setContent({ content: text, wordCount: words.length });
-      }
-    },
-    [limit, setContent]
-  );
-
-  React.useEffect(() => {
-    setFormattedContent(content);
-  }, []);
-
   return (
-    <>
-      <textarea
-        rows={rows}
-        cols={cols}
-        onChange={event => setFormattedContent(event.target.value)}
-        value={content}
-      />
-      <p>
-        {wordCount}/{limit}
-      </p>
-    </>
+    <Textarea
+      rows={rows}
+      cols={cols}
+      value={value}
+      readOnly
+      className="limited-textarea"
+      onChange={() => {}}
+    >
+      {value.length}/{limit}
+    </Textarea>
   );
 };
+
+export default LimitedWordTextarea;
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,39 +1,14 @@

 const LimitedWordTextarea = ({ rows, cols, value, limit }) => {
-  const [{ content, wordCount }, setContent] = React.useState({
-    content: value,
-    wordCount: 0
-  });
+  const [error, setError] = useState(false);
+  const [currentLength, setCurrentLength] = useState(0);
 
-  const setFormattedContent = React.useCallback(
-    text => {
-      let words = text.split(' ').filter(Boolean);
-      if (words.length > limit) {
-        setContent({
-          content: words.slice(0, limit).join(' '),
-          wordCount: limit
-        });
-      } else {
-        setContent({ content: text, wordCount: words.length });
-      }
-    },
-    [limit, setContent]
-  );
+  const onChange = ({ target: { value } }) => {
+    setCurrentLength(value.length);
+    if (value.length > limit) {
+      setError(true);
+    } else {
+      setError(false);
+    }
+  };
 
-  React.useEffect(() => {
-    setFormattedContent(content);
-  }, []);
-
-  return (
-    <>
-      <textarea
-        rows={rows}
-        cols={cols}
-        onChange={event => setFormattedContent(event.target.value)}
-        value={content}
-      />
-      <p>
-        {wordCount}/{limit}
-      </p>
-    </>
-  );
-};
+  const onBlur
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,39 +1,13 @@

 const LimitedWordTextarea = ({ rows, cols, value, limit }) => {
-  const [{ content, wordCount }, setContent] = React.useState({
-    content: value,
-    wordCount: 0
-  });
+  const [text, setText] = useState(value);
+  const [error, setError] = useState('');
 
-  const setFormattedContent = React.useCallback(
-    text => {
-      let words = text.split(' ').filter(Boolean);
-      if (words.length > limit) {
-        setContent({
-          content: words.slice(0, limit).join(' '),
-          wordCount: limit
-        });
-      } else {
-        setContent({ content: text, wordCount: words.length });
-      }
-    },
-    [limit, setContent]
-  );
-
-  React.useEffect(() => {
-    setFormattedContent(content);
-  }, []);
+  const onChange = e => {
+    const { value } = e.target;
+    setText(value);
+    setError(isValid(value, limit) ? '' : `Cannot exceed ${limit} characters`);
+  };
 
   return (
     <>
-      <textarea
-        rows={rows}
-        cols={cols}
-        onChange={event => setFormattedContent(event.target.value)}
-        value={content}
-      />
-      <p>
-        {wordCount}/{limit}
-      </p>
-    </>
-  );
-};
+      <Textarea
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,39 +1,9 @@

 const LimitedWordTextarea = ({ rows, cols, value, limit }) => {
-  const [{ content, wordCount }, setContent] = React.useState({
-    content: value,
-    wordCount: 0
-  });
+  const [currVal, setCurrVal] = useState(value);
+  const [count, setCount] = useState(value.length);
 
-  const setFormattedContent = React.useCallback(
-    text => {
-      let words = text.split(' ').filter(Boolean);
-      if (words.length > limit) {
-        setContent({
-          content: words.slice(0, limit).join(' '),
-          wordCount: limit
-        });
-      } else {
-        setContent({ content: text, wordCount: words.length });
-      }
-    },
-    [limit, setContent]
-  );
-
-  React.useEffect(() => {
-    setFormattedContent(content);
-  }, []);
-
-  return (
-    <>
-      <textarea
-        rows={rows}
-        cols={cols}
-        onChange={event => setFormattedContent(event.target.value)}
-        value={content}
-      />
-      <p>
-        {wordCount}/{limit}
-      </p>
-    </>
-  );
-};
+  const handleChange = (e) => {
+    const words = e.target.value.split(' ');
+    const textCount = words.filter((word) => word !== '').length;
+    setCurrVal(e.target.value);
+    setCount
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,39 +1,9 @@

 const LimitedWordTextarea = ({ rows, cols, value, limit }) => {
-  const [{ content, wordCount }, setContent] = React.useState({
-    content: value,
-    wordCount: 0
-  });
+  const [length, setLength] = useState(countSymbols(value));
+  const [count, setCount] = useState(countSymbols(value));
+  const [tempValue, setTempValue] = useState(value);
 
-  const setFormattedContent = React.useCallback(
-    text => {
-      let words = text.split(' ').filter(Boolean);
-      if (words.length > limit) {
-        setContent({
-          content: words.slice(0, limit).join(' '),
-          wordCount: limit
-        });
-      } else {
-        setContent({ content: text, wordCount: words.length });
-      }
-    },
-    [limit, setContent]
-  );
-
-  React.useEffect(() => {
-    setFormattedContent(content);
-  }, []);
-
-  return (
-    <>
-      <textarea
-        rows={rows}
-        cols={cols}
-        onChange={event => setFormattedContent(event.target.value)}
-        value={content}
-      />
-      <p>
-        {wordCount}/{limit}
-      </p>
-    </>
-  );
-};
+  const handleChange = ({ target: { value } }) => {
+    const newLength = countSymbols(value);
+    setTempValue(value);
+    setLength(new
```

### useOnWindowScroll (task/38)

#### canonical solution

```javascript
const useOnWindowScroll = callback => {
  const listener = React.useRef(null);

  React.useEffect(() => {
    if (listener.current)
      window.removeEventListener('scroll', listener.current);
    listener.current = window.addEventListener('scroll', callback);
    return () => {
      window.removeEventListener('scroll', listener.current);
    };
  }, [callback]);
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,12 +1,13 @@

 const useOnWindowScroll = callback => {
-  const listener = React.useRef(null);
-
-  React.useEffect(() => {
-    if (listener.current)
-      window.removeEventListener('scroll', listener.current);
-    listener.current = window.addEventListener('scroll', callback);
-    return () => {
-      window.removeEventListener('scroll', listener.current);
-    };
-  }, [callback]);
-};
+  const prevScrollTop = useRef(window.pageYOffset);
+  const handleScroll = () => {
+    const currentScrollTop = window.pageYOffset;
+    if (prevScrollTop.current < currentScrollTop) {
+      callback(true);
+    } else {
+      callback(false);
+    }
+    prevScrollTop.current = currentScrollTop;
+  };
+  useEffect(() => {
+    window
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,12 +1,13 @@

 const useOnWindowScroll = callback => {
-  const listener = React.useRef(null);
-
-  React.useEffect(() => {
-    if (listener.current)
-      window.removeEventListener('scroll', listener.current);
-    listener.current = window.addEventListener('scroll', callback);
+  const win = useWindow();
+  useEffect(() => {
+    const handleScroll = () => {
+      if (window.pageYOffset > callback.current) {
+        callback.current = window.pageYOffset;
+      }
+    };
+    win.addEventListener('scroll', handleScroll);
     return () => {
-      window.removeEventListener('scroll', listener.current);
+      win.removeEventListener('scroll', handleScroll);
     };
-  }, [callback]);
-};
+  }, [win]);
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,12 +1,13 @@

 const useOnWindowScroll = callback => {
-  const listener = React.useRef(null);
-
-  React.useEffect(() => {
-    if (listener.current)
-      window.removeEventListener('scroll', listener.current);
-    listener.current = window.addEventListener('scroll', callback);
-    return () => {
-      window.removeEventListener('scroll', listener.current);
-    };
+  useEffect(() => {
+    window.addEventListener('scroll', callback);
+    return () => window.removeEventListener('scroll', callback);
   }, [callback]);
 };
+
+export const useThrottle = (callback, delay) => {
+  const [, update] = useState(() => {
+    const timeout = setTimeout(callback, delay);
+    return () => clearTimeout(timeout);
+  });
+
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,12 +1,14 @@

 const useOnWindowScroll = callback => {
-  const listener = React.useRef(null);
+  const handleScroll = (e) => {
+    callback(e);
+  };
 
-  React.useEffect(() => {
-    if (listener.current)
-      window.removeEventListener('scroll', listener.current);
-    listener.current = window.addEventListener('scroll', callback);
+  useEffect(() => {
+    window.addEventListener('scroll', handleScroll);
     return () => {
-      window.removeEventListener('scroll', listener.current);
+      window.removeEventListener('scroll', handleScroll);
     };
-  }, [callback]);
+  }, []);
 };
+
+export default useOnWindowScroll;
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,12 +1,14 @@

 const useOnWindowScroll = callback => {
-  const listener = React.useRef(null);
+  const [isVisible, setIsVisible] = useState(true);
 
-  React.useEffect(() => {
-    if (listener.current)
-      window.removeEventListener('scroll', listener.current);
-    listener.current = window.addEventListener('scroll', callback);
+  useEffect(() => {
+    const handleScroll = () => {
+      const { scrollY } = window;
+      const isTop = scrollY < 40;
+      setIsVisible(isTop);
+    };
+
+    window.addEventListener('scroll', handleScroll);
+
     return () => {
-      window.removeEventListener('scroll', listener.current);
-    };
-  }, [callback]);
-};
+      window.removeEventListener('scroll',
```

### useClickInside (task/39)

#### canonical solution

```javascript
const useClickInside = (ref, callback) => {
  const handleClick = e => {
    if (ref.current && ref.current.contains(e.target)) {
      callback();
    }
  };
  React.useEffect(() => {
    document.addEventListener('click', handleClick);
    return () => {
      document.removeEventListener('click', handleClick);
    };
  });
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,13 +1,17 @@

 const useClickInside = (ref, callback) => {
-  const handleClick = e => {
-    if (ref.current && ref.current.contains(e.target)) {
-      callback();
-    }
-  };
-  React.useEffect(() => {
-    document.addEventListener('click', handleClick);
-    return () => {
-      document.removeEventListener('click', handleClick);
-    };
-  });
+    useEffect(() => {
+        const handleClick = (e) => {
+            if (ref.current && !ref.current.contains(e.target)) {
+                callback();
+            }
+        };
+
+        document.addEventListener('click', handleClick);
+
+        return () => {
+            document.removeEventListener('click', handleClick);
+        };
+    }, [ref, callback]);
 };
+
+export const
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,13 +1,17 @@

 const useClickInside = (ref, callback) => {
-  const handleClick = e => {
-    if (ref.current && ref.current.contains(e.target)) {
+  const handleClick = (e) => {
+    if (ref.current && !ref.current.contains(e.target)) {
       callback();
     }
   };
-  React.useEffect(() => {
+
+  useEffect(() => {
     document.addEventListener('click', handleClick);
+
     return () => {
       document.removeEventListener('click', handleClick);
     };
   });
 };
+
+export default useClickInside;
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,13 +1,15 @@

 const useClickInside = (ref, callback) => {
-  const handleClick = e => {
-    if (ref.current && ref.current.contains(e.target)) {
-      callback();
-    }
-  };
-  React.useEffect(() => {
-    document.addEventListener('click', handleClick);
+    const listener = event => {
+        if (!ref.current || ref.current.contains(event.target)) {
+            return;
+        }
+        callback(event);
+    };
+    document.addEventListener('click', listener);
     return () => {
-      document.removeEventListener('click', handleClick);
+        document.removeEventListener('click', listener);
     };
-  });
 };
+
+const useOutsideClick = (ref, callback) => {
+    const listener = event
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,13 +1,18 @@

 const useClickInside = (ref, callback) => {
   const handleClick = e => {
-    if (ref.current && ref.current.contains(e.target)) {
+    if (ref.current && !ref.current.contains(e.target)) {
       callback();
     }
   };
-  React.useEffect(() => {
-    document.addEventListener('click', handleClick);
+
+  useEffect(() => {
+    document.addEventListener("click", handleClick);
+
     return () => {
-      document.removeEventListener('click', handleClick);
+      document.removeEventListener("click", handleClick);
     };
   });
 };
+
+const inputPlaceholder = {
+  "
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,13 +1,17 @@

 const useClickInside = (ref, callback) => {
-  const handleClick = e => {
-    if (ref.current && ref.current.contains(e.target)) {
-      callback();
+    const handleClick = e => {
+        if (ref.current && !ref.current.contains(e.target)) {
+            callback()
+        }
     }
-  };
-  React.useEffect(() => {
-    document.addEventListener('click', handleClick);
-    return () => {
-      document.removeEventListener('click', handleClick);
-    };
-  });
-};
+
+    useEffect(() => {
+        document.addEventListener('click', handleClick)
+
+        return () => {
+            document.removeEventListener('click', handleClick)
+        }
+    })
+}
+
+export default useClickInside
```

### useSSR (task/40)

#### canonical solution

```javascript
const isDOMavailable = !!(
  typeof window !== 'undefined' &&
  window.document &&
  window.document.createElement
);

const useSSR = () => {
  const [inBrowser, setInBrowser] = React.useState(isDOMavailable);

  React.useEffect(() => {
    setInBrowser(isDOMavailable);
    return () => {
      setInBrowser(false);
    };
  }, []);

  const useSSRObject = React.useMemo(
    () => ({
      isBrowser: inBrowser,
      isServer: !inBrowser,
      canUseWorkers: typeof Worker !== 'undefined',
      canUseEventListeners: inBrowser && !!window.addEventListener,
      canUseViewport: inBrowser && !!window.screen
    }),
    [inBrowser]
  );

  return React.useMemo(
    () => Object.assign(Object.values(useSSRObject), useSSRObject),
    [inBrowser]
  );
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -4,29 +4,8 @@

   window.document.createElement
 );
 
-const useSSR = () => {
-  const [inBrowser, setInBrowser] = React.useState(isDOMavailable);
+export const isSafari = isDOMavailable && /^((?!chrome|android).)*safari/i.test(navigator.userAgent);
 
-  React.useEffect(() => {
-    setInBrowser(isDOMavailable);
-    return () => {
-      setInBrowser(false);
-    };
-  }, []);
+export const isChrome = isDOMavailable && /^chrome.*safari/i.test(navigator.userAgent);
 
-  const useSSRObject = React.useMemo(
-    () => ({
-      isBrowser: inBrowser,
-      isServer: !inBrowser,
-      canUseWorkers: typeof Worker !== 'undefined',
-      canUseEventListeners: inBrowser && !!window.addEventListener,
-      canUseViewport: inBrowser && !!window.screen
-    }),
-    [inBrowser]
-  );
-
-  return React.useMemo(
-    () => Object.assign(Object.values(useSSRObject), useSSRObject),
-    [inBrowser]
-  );
-};
+export const isChrome
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,31 +1,12 @@

-const isDOMavailable = !!(  typeof window !== 'undefined' &&
-  window.document &&
-  window.document.createElement
-);
+const isDOMavailable = !!(typeof window !== 'undefined' && window.document && window.document.createElement);
 
-const useSSR = () => {
-  const [inBrowser, setInBrowser] = React.useState(isDOMavailable);
-
-  React.useEffect(() => {
-    setInBrowser(isDOMavailable);
-    return () => {
-      setInBrowser(false);
-    };
-  }, []);
-
-  const useSSRObject = React.useMemo(
-    () => ({
-      isBrowser: inBrowser,
-      isServer: !inBrowser,
-      canUseWorkers: typeof Worker !== 'undefined',
-      canUseEventListeners: inBrowser && !!window.addEventListener,
-      canUseViewport: inBrowser && !!window.screen
-    }),
-    [inBrowser]
-  );
-
-  return React.useMemo(
-    () => Object.assign(Object.values(useSSRObject), useSSRObject),
-    [inBrowser]
-  );
-};
+/**
+ * Map to convert svg filters to webgl filters.
+ */
+const SVG_FILTERS = {
+  'blur': 0,
+  'brightness': 1,
+  'contrast': 2,
+  'grayscale': 3,
+  'hueRotate': 4,
+  'invert': 5,
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -4,29 +4,12 @@

   window.document.createElement
 );
 
-const useSSR = () => {
-  const [inBrowser, setInBrowser] = React.useState(isDOMavailable);
+const addEventListener = (element, event, handler) => {
+  if (isDOMavailable) {
+    element.addEventListener(event, handler);
+  }
+};
 
-  React.useEffect(() => {
-    setInBrowser(isDOMavailable);
-    return () => {
-      setInBrowser(false);
-    };
-  }, []);
-
-  const useSSRObject = React.useMemo(
-    () => ({
-      isBrowser: inBrowser,
-      isServer: !inBrowser,
-      canUseWorkers: typeof Worker !== 'undefined',
-      canUseEventListeners: inBrowser && !!window.addEventListener,
-      canUseViewport: inBrowser && !!window.screen
-    }),
-    [inBrowser]
-  );
-
-  return React.useMemo(
-    () => Object.assign(Object.values(useSSRObject), useSSRObject),
-    [inBrowser]
-  );
-};
+const removeEventListener = (element, event, handler) => {
+  if (isDOMavailable) {
+    element.
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -4,29 +4,8 @@

   window.document.createElement
 );
 
-const useSSR = () => {
-  const [inBrowser, setInBrowser] = React.useState(isDOMavailable);
+const getConfigFromMetaTag = (html: string): Config | null => {
+  const regex = /<meta [^>]*name="recharts_config" [^>]*content="([^"]*)"/i;
+  const meta = html.match(regex);
 
-  React.useEffect(() => {
-    setInBrowser(isDOMavailable);
-    return () => {
-      setInBrowser(false);
-    };
-  }, []);
-
-  const useSSRObject = React.useMemo(
-    () => ({
-      isBrowser: inBrowser,
-      isServer: !inBrowser,
-      canUseWorkers: typeof Worker !== 'undefined',
-      canUseEventListeners: inBrowser && !!window.addEventListener,
-      canUseViewport: inBrowser && !!window.screen
-    }),
-    [inBrowser]
-  );
-
-  return React.useMemo(
-    () => Object.assign(Object.values(useSSRObject), useSSRObject),
-    [inBrowser]
-  );
-};
+  if (meta &&
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -4,29 +4,15 @@

   window.document.createElement
 );
 
-const useSSR = () => {
-  const [inBrowser, setInBrowser] = React.useState(isDOMavailable);
+export function createPortal(
+  children: React.ReactNode,
+  container: Element | null,
+  forceNew?: boolean,
+): Element | null {
+  if (!isDOMavailable) {
+    return null;
+  }
 
-  React.useEffect(() => {
-    setInBrowser(isDOMavailable);
-    return () => {
-      setInBrowser(false);
-    };
-  }, []);
-
-  const useSSRObject = React.useMemo(
-    () => ({
-      isBrowser: inBrowser,
-      isServer: !inBrowser,
-      canUseWorkers: typeof Worker !== 'undefined',
-      canUseEventListeners: inBrowser && !!window.addEventListener,
-      canUseViewport: inBrowser && !!window.screen
-    }),
-    [inBrowser]
-  );
-
-  return React.useMemo(
-    () => Object.assign(Object.values(useSSRObject), useSSRObject),
-    [inBrowser]
-  );
-};
+  if (!container) {
+    return null;
+  }
```

### LimitedTextarea (task/41)

#### canonical solution

```javascript
const LimitedTextarea = ({ rows, cols, value, limit }) => {
  const [content, setContent] = React.useState(value.slice(0, limit));

  const setFormattedContent = React.useCallback(
    text => {
      setContent(text.slice(0, limit));
    },
    [limit, setContent]
  );

  return (
    <>
      <textarea
        rows={rows}
        cols={cols}
        onChange={event => setFormattedContent(event.target.value)}
        value={content}
      />
      <p>
        {content.length}/{limit}
      </p>
    </>
  );
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,24 +1,13 @@

 const LimitedTextarea = ({ rows, cols, value, limit }) => {
-  const [content, setContent] = React.useState(value.slice(0, limit));
+  const [count, setCount] = useState(value.length);
+  const [text, setText] = useState(value);
 
-  const setFormattedContent = React.useCallback(
-    text => {
-      setContent(text.slice(0, limit));
-    },
-    [limit, setContent]
-  );
+  useEffect(() => {
+    setCount(value.length);
+    setText(value);
+  }, [value]);
 
-  return (
-    <>
-      <textarea
-        rows={rows}
-        cols={cols}
-        onChange={event => setFormattedContent(event.target.value)}
-        value={content}
-      />
-      <p>
-        {content.length}/{limit}
-      </p>
-    </>
-  );
-};
+  const removeLastChar = (e) => {
+    e.preventDefault();
+    setCount(count - 1);
+    setText(text.slice
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,24 +1,11 @@

 const LimitedTextarea = ({ rows, cols, value, limit }) => {
-  const [content, setContent] = React.useState(value.slice(0, limit));
+  const [visibleText, setVisibleText] = useState(value);
+  const [isOverLimit, setIsOverLimit] = useState(false);
 
-  const setFormattedContent = React.useCallback(
-    text => {
-      setContent(text.slice(0, limit));
-    },
-    [limit, setContent]
-  );
-
-  return (
-    <>
-      <textarea
-        rows={rows}
-        cols={cols}
-        onChange={event => setFormattedContent(event.target.value)}
-        value={content}
-      />
-      <p>
-        {content.length}/{limit}
-      </p>
-    </>
-  );
-};
+  useEffect(() => {
+    if (value && value.length > limit) {
+      setVisibleText(value.substring(0, limit));
+      setIsOverLimit(true);
+    } else {
+      setVisibleText(value);
+     
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,24 +1,12 @@

 const LimitedTextarea = ({ rows, cols, value, limit }) => {
-  const [content, setContent] = React.useState(value.slice(0, limit));
+  const [text, setText] = useState(value)
+  const [textCount, setTextCount] = useState(value.length)
 
-  const setFormattedContent = React.useCallback(
-    text => {
-      setContent(text.slice(0, limit));
-    },
-    [limit, setContent]
-  );
+  useEffect(() => {
+    setText(value)
+    setTextCount(value.length)
+  }, [value])
 
-  return (
-    <>
-      <textarea
-        rows={rows}
-        cols={cols}
-        onChange={event => setFormattedContent(event.target.value)}
-        value={content}
-      />
-      <p>
-        {content.length}/{limit}
-      </p>
-    </>
-  );
-};
+  const handleChange = e => {
+    setText(e.target.value)
+    setTextCount(e.target.value.length)
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,24 +1,15 @@

 const LimitedTextarea = ({ rows, cols, value, limit }) => {
-  const [content, setContent] = React.useState(value.slice(0, limit));
+  const [text, setText] = useState(value);
+  const [count, setCount] = useState(0);
 
-  const setFormattedContent = React.useCallback(
-    text => {
-      setContent(text.slice(0, limit));
-    },
-    [limit, setContent]
-  );
+  const changeText = (e) => {
+    setText(e.target.value);
+    setCount(e.target.value.length);
+  };
+
+  const resetText = () => {
+    setText(value);
+    setCount(0);
+  };
 
   return (
-    <>
-      <textarea
-        rows={rows}
-        cols={cols}
-        onChange={event => setFormattedContent(event.target.value)}
-        value={content}
-      />
-      <p>
-        {content.length}/{limit}
-      </p>
-    </>
-  );
-};
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,24 +1,12 @@

 const LimitedTextarea = ({ rows, cols, value, limit }) => {
-  const [content, setContent] = React.useState(value.slice(0, limit));
+  const classes = useStyles();
+  const [text, setText] = useState(value);
+  const [end, setEnd] = useState(false);
 
-  const setFormattedContent = React.useCallback(
-    text => {
-      setContent(text.slice(0, limit));
-    },
-    [limit, setContent]
-  );
-
-  return (
-    <>
-      <textarea
-        rows={rows}
-        cols={cols}
-        onChange={event => setFormattedContent(event.target.value)}
-        value={content}
-      />
-      <p>
-        {content.length}/{limit}
-      </p>
-    </>
-  );
-};
+  const handleChange = (e) => {
+    const { value } = e.target;
+    if (value.length > limit) {
+      setText(value.slice(0, limit));
+      setEnd(true);
+    } else {
+     
```

### useComponentDidMount (task/42)

#### canonical solution

```javascript
const useComponentDidMount = onMountHandler => {
  React.useEffect(() => {
    onMountHandler();
  }, []);
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,5 +1,10 @@

 const useComponentDidMount = onMountHandler => {
-  React.useEffect(() => {
-    onMountHandler();
+  return useEffect(() => {
+    if (onMountHandler) {
+      onMountHandler();
+    }
   }, []);
 };
+
+export const useComponentWillUnmount = onUnmountHandler => {
+  return useEffect(() => {
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,5 +1,7 @@

 const useComponentDidMount = onMountHandler => {
-  React.useEffect(() => {
+  return useEffect(() => {
     onMountHandler();
   }, []);
 };
+
+export default useComponentDidMount;
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,5 +1,9 @@

 const useComponentDidMount = onMountHandler => {
-  React.useEffect(() => {
-    onMountHandler();
-  }, []);
-};
+  const handleComponentDidMount = () => {
+    onMountHandler()
+  }
+
+  return handleComponentDidMount
+}
+
+export default useComponentDidMount
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,5 +1,10 @@

 const useComponentDidMount = onMountHandler => {
-  React.useEffect(() => {
+  useEffect(() => {
     onMountHandler();
   }, []);
 };
+
+const useComponentWillUnmount = onUnmountHandler => {
+  useEffect(() => {
+    return () => {
+      onUnmountHandler();
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,5 +1,7 @@

 const useComponentDidMount = onMountHandler => {
-  React.useEffect(() => {
+  useEffect(() => {
     onMountHandler();
   }, []);
 };
+
+export default useComponentDidMount;
```

### FileDrop (task/43)

#### canonical solution

```javascript
const FileDrop = ({ onDrop }) => {
  const [drag, setDrag] = React.useState(false);
  const [filename, setFilename] = React.useState('');
  let dropRef = React.createRef();
  let dragCounter = 0;

  const handleDrag = e => {
    e.preventDefault();
    e.stopPropagation();
  };

  const handleDragIn = e => {
    e.preventDefault();
    e.stopPropagation();
    dragCounter++;
    if (e.dataTransfer.items && e.dataTransfer.items.length > 0) setDrag(true);
  };

  const handleDragOut = e => {
    e.preventDefault();
    e.stopPropagation();
    dragCounter--;
    if (dragCounter === 0) setDrag(false);
  };

  const handleDrop = e => {
    e.preventDefault();
    e.stopPropagation();
    setDrag(false);
    if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {
      onDrop(e.dataTransfer.files[0]);
      setFilename(e.dataTransfer.files[0].name);
      e.dataTransfer.clearData();
      dragCounter = 0;
    }
  };

  React.useEffect(() => {
    let div = dropRef.current;
    div.addEventListener('dragenter', handleDragIn);
    div.addEventListener('dragleave', handleDragOut);
    div.addEventListener('dragover', handleDrag);
    div.addEventListener('drop', handleDrop);
    return () => {
      div.removeEventListener('dragenter', handleDragIn);
      div.removeEventListener('dragleave', handleDragOut);
      div.removeEventListener('dragover', handleDrag);
      div.removeEventListener('drop', handleDrop);
    };
  });

  return (
    <div
      ref={dropRef}
      className={
        drag ? 'filedrop drag' : filename ? 'filedrop ready' : 'filedrop'
      }
    >
      {filename && !drag ? <div>{filename}</div> : <div>Drop a file here!</div>}
    </div>
  );
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,62 +1,17 @@

 const FileDrop = ({ onDrop }) => {
-  const [drag, setDrag] = React.useState(false);
-  const [filename, setFilename] = React.useState('');
-  let dropRef = React.createRef();
-  let dragCounter = 0;
+  const dropRef = useRef(null);
 
-  const handleDrag = e => {
+  const handleDrop = (e) => {
     e.preventDefault();
-    e.stopPropagation();
+    onDrop(e.dataTransfer.files);
   };
 
-  const handleDragIn = e => {
+  const handleDragOver = (e) => {
     e.preventDefault();
-    e.stopPropagation();
-    dragCounter++;
-    if (e.dataTransfer.items && e.dataTransfer.items.length > 0) setDrag(true);
   };
-
-  const handleDragOut = e => {
-    e.preventDefault();
-    e.stopPropagation();
-    dragCounter--;
-    if (dragCounter === 0) setDrag(false);
-  };
-
-  const handleDrop = e => {
-    e.preventDefault();
-    e.stopPropagation();
-    setDrag(false);
-    if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {
-      onDrop(e.dataTransfer.files[0]);
-      setFilename(e.dataTransfer.files[0].name);
-      e.dataTransfer.clearData();
-      dragCounter = 0;
-    }
-  };
-
-  React.useEffect(() => {
-    let div = dropRef.current;
-    div.addEventListener('dragenter', handleDragIn);
-    div.addEventListener('dragleave', handleDragOut);
-    div.addEventListener('dragover', handleDrag);
-    div.addEventListener('drop', handleDrop);
-    return () => {
-      div.removeEventListener('dragenter', handleDragIn);
-      div.removeEventListener('dragleave', handleDragOut);
-      div.removeEventListener('dragover', handleDrag);
-      div.removeEventListener('drop', handleDrop);
-    };
-  });
 
   return (
     <div
+      className="drop-box"
       ref={dropRef}
-      className={
-        drag ? 'filedrop drag' : filename ? 'filedrop ready' : 'filedrop'
-      }
-    >
-      {filename && !drag ? <div>{filename}</div> : <div>Drop a file here!</div>}
-    </div>
-  );
-};
+      onDrop={handleDrop
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,62 +1,15 @@

 const FileDrop = ({ onDrop }) => {
-  const [drag, setDrag] = React.useState(false);
-  const [filename, setFilename] = React.useState('');
-  let dropRef = React.createRef();
-  let dragCounter = 0;
+  const [file, setFile] = useState();
+  const [error, setError] = useState();
 
-  const handleDrag = e => {
-    e.preventDefault();
-    e.stopPropagation();
-  };
+  const onChange = useCallback(
+    (e) => {
+      const { files } = e.target;
+      if (files && files.length > 0) {
+        setFile(files[0]);
+      }
+    },
+    [setFile]
+  );
 
-  const handleDragIn = e => {
-    e.preventDefault();
-    e.stopPropagation();
-    dragCounter++;
-    if (e.dataTransfer.items && e.dataTransfer.items.length > 0) setDrag(true);
-  };
-
-  const handleDragOut = e => {
-    e.preventDefault();
-    e.stopPropagation();
-    dragCounter--;
-    if (dragCounter === 0) setDrag(false);
-  };
-
-  const handleDrop = e => {
-    e.preventDefault();
-    e.stopPropagation();
-    setDrag(false);
-    if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {
-      onDrop(e.dataTransfer.files[0]);
-      setFilename(e.dataTransfer.files[0].name);
-      e.dataTransfer.clearData();
-      dragCounter = 0;
-    }
-  };
-
-  React.useEffect(() => {
-    let div = dropRef.current;
-    div.addEventListener('dragenter', handleDragIn);
-    div.addEventListener('dragleave', handleDragOut);
-    div.addEventListener('dragover', handleDrag);
-    div.addEventListener('drop', handleDrop);
-    return () => {
-      div.removeEventListener('dragenter', handleDragIn);
-      div.removeEventListener('dragleave', handleDragOut);
-      div.removeEventListener('dragover', handleDrag);
-      div.removeEventListener('drop', handleDrop);
-    };
-  });
-
-  return (
-    <div
-      ref={dropRef}
-      className={
-        drag ? 'filedrop drag' : filename ? 'filedrop ready' : 'filedrop'
-      }
-    >
-      {filename && !drag ? <div>{filename}</div> : <div>Drop a file here!</div>}
-    </div>
-  );
-};
+  const onDropHandler = useCallback
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,62 +1,17 @@

 const FileDrop = ({ onDrop }) => {
-  const [drag, setDrag] = React.useState(false);
-  const [filename, setFilename] = React.useState('');
-  let dropRef = React.createRef();
-  let dragCounter = 0;
-
-  const handleDrag = e => {
+  const onDragOver = e => {
     e.preventDefault();
-    e.stopPropagation();
   };
 
-  const handleDragIn = e => {
+  const onDropHandler = e => {
     e.preventDefault();
-    e.stopPropagation();
-    dragCounter++;
-    if (e.dataTransfer.items && e.dataTransfer.items.length > 0) setDrag(true);
+    onDrop(e.dataTransfer.files);
   };
-
-  const handleDragOut = e => {
-    e.preventDefault();
-    e.stopPropagation();
-    dragCounter--;
-    if (dragCounter === 0) setDrag(false);
-  };
-
-  const handleDrop = e => {
-    e.preventDefault();
-    e.stopPropagation();
-    setDrag(false);
-    if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {
-      onDrop(e.dataTransfer.files[0]);
-      setFilename(e.dataTransfer.files[0].name);
-      e.dataTransfer.clearData();
-      dragCounter = 0;
-    }
-  };
-
-  React.useEffect(() => {
-    let div = dropRef.current;
-    div.addEventListener('dragenter', handleDragIn);
-    div.addEventListener('dragleave', handleDragOut);
-    div.addEventListener('dragover', handleDrag);
-    div.addEventListener('drop', handleDrop);
-    return () => {
-      div.removeEventListener('dragenter', handleDragIn);
-      div.removeEventListener('dragleave', handleDragOut);
-      div.removeEventListener('dragover', handleDrag);
-      div.removeEventListener('drop', handleDrop);
-    };
-  });
 
   return (
     <div
-      ref={dropRef}
-      className={
-        drag ? 'filedrop drag' : filename ? 'filedrop ready' : 'filedrop'
-      }
+      onDragOver={onDragOver}
+      onDrop={onDropHandler}
+      className="dropzone-container"
     >
-      {filename && !drag ? <div>{filename}</div> : <div>Drop a file here!</div>}
-    </div>
-  );
-};
+      <div class
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,62 +1,15 @@

 const FileDrop = ({ onDrop }) => {
-  const [drag, setDrag] = React.useState(false);
-  const [filename, setFilename] = React.useState('');
-  let dropRef = React.createRef();
-  let dragCounter = 0;
+  const [dragOver, setDragOver] = useState(false);
 
-  const handleDrag = e => {
+  const onDragOver = (e) => {
     e.preventDefault();
-    e.stopPropagation();
+    setDragOver(true);
   };
 
-  const handleDragIn = e => {
-    e.preventDefault();
-    e.stopPropagation();
-    dragCounter++;
-    if (e.dataTransfer.items && e.dataTransfer.items.length > 0) setDrag(true);
+  const onDragLeave = () => {
+    setDragOver(false);
   };
 
-  const handleDragOut = e => {
-    e.preventDefault();
-    e.stopPropagation();
-    dragCounter--;
-    if (dragCounter === 0) setDrag(false);
-  };
-
-  const handleDrop = e => {
-    e.preventDefault();
-    e.stopPropagation();
-    setDrag(false);
-    if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {
-      onDrop(e.dataTransfer.files[0]);
-      setFilename(e.dataTransfer.files[0].name);
-      e.dataTransfer.clearData();
-      dragCounter = 0;
-    }
-  };
-
-  React.useEffect(() => {
-    let div = dropRef.current;
-    div.addEventListener('dragenter', handleDragIn);
-    div.addEventListener('dragleave', handleDragOut);
-    div.addEventListener('dragover', handleDrag);
-    div.addEventListener('drop', handleDrop);
-    return () => {
-      div.removeEventListener('dragenter', handleDragIn);
-      div.removeEventListener('dragleave', handleDragOut);
-      div.removeEventListener('dragover', handleDrag);
-      div.removeEventListener('drop', handleDrop);
-    };
-  });
-
-  return (
-    <div
-      ref={dropRef}
-      className={
-        drag ? 'filedrop drag' : filename ? 'filedrop ready' : 'filedrop'
-      }
-    >
-      {filename && !drag ? <div>{filename}</div> : <div>Drop a file here!</div>}
-    </div>
-  );
-};
+  const onDropHandler = (e) => {
+    onDrop(e.dataTransfer.files);
+    setDragOver
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,62 +1,11 @@

 const FileDrop = ({ onDrop }) => {
-  const [drag, setDrag] = React.useState(false);
-  const [filename, setFilename] = React.useState('');
-  let dropRef = React.createRef();
-  let dragCounter = 0;
+  const [uploading, setUploading] = useState(false);
+  const [file, setFile] = useState(null);
+  const [filename, setFilename] = useState(null);
+  const [error, setError] = useState(null);
 
-  const handleDrag = e => {
-    e.preventDefault();
-    e.stopPropagation();
-  };
-
-  const handleDragIn = e => {
-    e.preventDefault();
-    e.stopPropagation();
-    dragCounter++;
-    if (e.dataTransfer.items && e.dataTransfer.items.length > 0) setDrag(true);
-  };
-
-  const handleDragOut = e => {
-    e.preventDefault();
-    e.stopPropagation();
-    dragCounter--;
-    if (dragCounter === 0) setDrag(false);
-  };
-
-  const handleDrop = e => {
-    e.preventDefault();
-    e.stopPropagation();
-    setDrag(false);
-    if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {
-      onDrop(e.dataTransfer.files[0]);
-      setFilename(e.dataTransfer.files[0].name);
-      e.dataTransfer.clearData();
-      dragCounter = 0;
-    }
-  };
-
-  React.useEffect(() => {
-    let div = dropRef.current;
-    div.addEventListener('dragenter', handleDragIn);
-    div.addEventListener('dragleave', handleDragOut);
-    div.addEventListener('dragover', handleDrag);
-    div.addEventListener('drop', handleDrop);
-    return () => {
-      div.removeEventListener('dragenter', handleDragIn);
-      div.removeEventListener('dragleave', handleDragOut);
-      div.removeEventListener('dragover', handleDrag);
-      div.removeEventListener('drop', handleDrop);
-    };
-  });
-
-  return (
-    <div
-      ref={dropRef}
-      className={
-        drag ? 'filedrop drag' : filename ? 'filedrop ready' : 'filedrop'
-      }
-    >
-      {filename && !drag ? <div>{filename}</div> : <div>Drop a file here!</div>}
-    </div>
-  );
-};
+  const handleDrop = (acceptedFiles) => {
+    setUploading(true);
+    setFilename(null);
+    setError(null);
+   
```

### TreeView (task/44)

#### canonical solution

```javascript
const TreeView = ({
  data,
  toggled = true,
  name = null,
  isLast = true,
  isChildElement = false,
  isParentToggled = true
}) => {
  const [isToggled, setIsToggled] = React.useState(toggled);
  const isDataArray = Array.isArray(data);

  return (
    <div
      className={`tree-element ${isParentToggled && 'collapsed'} ${
        isChildElement && 'is-child'
      }`}
    >
      <span
        className={isToggled ? 'toggler' : 'toggler closed'}
        onClick={() => setIsToggled(!isToggled)}
      />
      {name ? <strong>&nbsp;&nbsp;{name}: </strong> : <span>&nbsp;&nbsp;</span>}
      {isDataArray ? '[' : '{'}
      {!isToggled && '...'}
      {Object.keys(data).map((v, i, a) =>
        typeof data[v] === 'object' ? (
          <TreeView
            key={`${name}-${v}-${i}`}
            data={data[v]}
            isLast={i === a.length - 1}
            name={isDataArray ? null : v}
            isChildElement
            isParentToggled={isParentToggled && isToggled}
          />
        ) : (
          <p
            key={`${name}-${v}-${i}`}
            className={isToggled ? 'tree-element' : 'tree-element collapsed'}
          >
            {isDataArray ? '' : <strong>{v}: </strong>}
            {data[v]}
            {i === a.length - 1 ? '' : ','}
          </p>
        )
      )}
      {isDataArray ? ']' : '}'}
      {!isLast ? ',' : ''}
    </div>
  );
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,50 +1,18 @@

 const TreeView = ({
-  data,
-  toggled = true,
-  name = null,
-  isLast = true,
-  isChildElement = false,
-  isParentToggled = true
+  name,
+  url,
+  children,
+  icon,
+  className,
+  activeClassName,
+  activeOnlyWhenExact,
+  activeStyle,
+  style,
+  isActive,
+  depth,
+  ...rest
 }) => {
-  const [isToggled, setIsToggled] = React.useState(toggled);
-  const isDataArray = Array.isArray(data);
-
-  return (
-    <div
-      className={`tree-element ${isParentToggled && 'collapsed'} ${
-        isChildElement && 'is-child'
-      }`}
-    >
-      <span
-        className={isToggled ? 'toggler' : 'toggler closed'}
-        onClick={() => setIsToggled(!isToggled)}
-      />
-      {name ? <strong>&nbsp;&nbsp;{name}: </strong> : <span>&nbsp;&nbsp;</span>}
-      {isDataArray ? '[' : '{'}
-      {!isToggled && '...'}
-      {Object.keys(data).map((v, i, a) =>
-        typeof data[v] === 'object' ? (
-          <TreeView
-            key={`${name}-${v}-${i}`}
-            data={data[v]}
-            isLast={i === a.length - 1}
-            name={isDataArray ? null : v}
-            isChildElement
-            isParentToggled={isParentToggled && isToggled}
-          />
-        ) : (
-          <p
-            key={`${name}-${v}-${i}`}
-            className={isToggled ? 'tree-element' : 'tree-element collapsed'}
-          >
-            {isDataArray ? '' : <strong>{v}: </strong>}
-            {data[v]}
-            {i === a.length - 1 ? '' : ','}
-          </p>
-        )
-      )}
-      {isDataArray ? ']' : '}'}
-      {!isLast ? ',' : ''}
-    </div>
-  );
-};
+  const isActiveProps = isActive ? { activeClassName, activeStyle, isActive } : {};
+  const routeProps = {
+    name,
+   
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,50 +1,19 @@

 const TreeView = ({
-  data,
-  toggled = true,
-  name = null,
-  isLast = true,
-  isChildElement = false,
-  isParentToggled = true
+  // context
+  name, required, strict, depth,
+  // state
+  state, path, formName,
+  // actions
+  actions,
+  //
+  list, listPath, listActions,
+  item, itemPath, itemActions,
+  //
+  onChange,
+  children,
+  //
+  className,
+  ...props
 }) => {
-  const [isToggled, setIsToggled] = React.useState(toggled);
-  const isDataArray = Array.isArray(data);
-
-  return (
-    <div
-      className={`tree-element ${isParentToggled && 'collapsed'} ${
-        isChildElement && 'is-child'
-      }`}
-    >
-      <span
-        className={isToggled ? 'toggler' : 'toggler closed'}
-        onClick={() => setIsToggled(!isToggled)}
-      />
-      {name ? <strong>&nbsp;&nbsp;{name}: </strong> : <span>&nbsp;&nbsp;</span>}
-      {isDataArray ? '[' : '{'}
-      {!isToggled && '...'}
-      {Object.keys(data).map((v, i, a) =>
-        typeof data[v] === 'object' ? (
-          <TreeView
-            key={`${name}-${v}-${i}`}
-            data={data[v]}
-            isLast={i === a.length - 1}
-            name={isDataArray ? null : v}
-            isChildElement
-            isParentToggled={isParentToggled && isToggled}
-          />
-        ) : (
-          <p
-            key={`${name}-${v}-${i}`}
-            className={isToggled ? 'tree-element' : 'tree-element collapsed'}
-          >
-            {isDataArray ? '' : <strong>{v}: </strong>}
-            {data[v]}
-            {i === a.length - 1 ? '' : ','}
-          </p>
-        )
-      )}
-      {isDataArray ? ']' : '}'}
-      {!isLast ? ',' : ''}
-    </div>
-  );
-};
+  const {
+    autoFocus, disabled,
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,49 +1,10 @@

-const TreeView = ({  data,
-  toggled = true,
-  name = null,
-  isLast = true,
-  isChildElement = false,
-  isParentToggled = true
-}) => {
-  const [isToggled, setIsToggled] = React.useState(toggled);
-  const isDataArray = Array.isArray(data);
+const TreeView = ({ className, data, onSelect, getKey, getText, getIcon, onDoubleClick, onRightClick, onExpand }) => {
+  const onSelectInternal = (item, event) => {
+    if (onSelect) {
+      onSelect(item, event);
+    }
+  };
 
-  return (
-    <div
-      className={`tree-element ${isParentToggled && 'collapsed'} ${
-        isChildElement && 'is-child'
-      }`}
-    >
-      <span
-        className={isToggled ? 'toggler' : 'toggler closed'}
-        onClick={() => setIsToggled(!isToggled)}
-      />
-      {name ? <strong>&nbsp;&nbsp;{name}: </strong> : <span>&nbsp;&nbsp;</span>}
-      {isDataArray ? '[' : '{'}
-      {!isToggled && '...'}
-      {Object.keys(data).map((v, i, a) =>
-        typeof data[v] === 'object' ? (
-          <TreeView
-            key={`${name}-${v}-${i}`}
-            data={data[v]}
-            isLast={i === a.length - 1}
-            name={isDataArray ? null : v}
-            isChildElement
-            isParentToggled={isParentToggled && isToggled}
-          />
-        ) : (
-          <p
-            key={`${name}-${v}-${i}`}
-            className={isToggled ? 'tree-element' : 'tree-element collapsed'}
-          >
-            {isDataArray ? '' : <strong>{v}: </strong>}
-            {data[v]}
-            {i === a.length - 1 ? '' : ','}
-          </p>
-        )
-      )}
-      {isDataArray ? ']' : '}'}
-      {!isLast ? ',' : ''}
-    </div>
-  );
-};
+  const onDoubleClickInternal = (item, event) => {
+    if (onDoubleClick) {
+      onDoubleClick(item,
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,49 +1,5 @@

-const TreeView = ({  data,
-  toggled = true,
-  name = null,
-  isLast = true,
-  isChildElement = false,
-  isParentToggled = true
-}) => {
-  const [isToggled, setIsToggled] = React.useState(toggled);
-  const isDataArray = Array.isArray(data);
-
-  return (
-    <div
-      className={`tree-element ${isParentToggled && 'collapsed'} ${
-        isChildElement && 'is-child'
-      }`}
-    >
-      <span
-        className={isToggled ? 'toggler' : 'toggler closed'}
-        onClick={() => setIsToggled(!isToggled)}
-      />
-      {name ? <strong>&nbsp;&nbsp;{name}: </strong> : <span>&nbsp;&nbsp;</span>}
-      {isDataArray ? '[' : '{'}
-      {!isToggled && '...'}
-      {Object.keys(data).map((v, i, a) =>
-        typeof data[v] === 'object' ? (
-          <TreeView
-            key={`${name}-${v}-${i}`}
-            data={data[v]}
-            isLast={i === a.length - 1}
-            name={isDataArray ? null : v}
-            isChildElement
-            isParentToggled={isParentToggled && isToggled}
-          />
-        ) : (
-          <p
-            key={`${name}-${v}-${i}`}
-            className={isToggled ? 'tree-element' : 'tree-element collapsed'}
-          >
-            {isDataArray ? '' : <strong>{v}: </strong>}
-            {data[v]}
-            {i === a.length - 1 ? '' : ','}
-          </p>
-        )
-      )}
-      {isDataArray ? ']' : '}'}
-      {!isLast ? ',' : ''}
-    </div>
-  );
-};
+const TreeView = ({ root, header, onClick, onToggle, onDoubleClick, getItemProps, getItemPropsOfSelectedItem, renderItem, renderSelectedItem, renderExpandedItem, onClickItem }) => {
+  const [, theme] = useStyletron();
+  const classes = useTreeViewClasses({ theme });
+  const [selected, setSelected] = useState([]);
+  const [expanded, setExpanded
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,50 +1,12 @@

 const TreeView = ({
+  className,
   data,
-  toggled = true,
-  name = null,
-  isLast = true,
-  isChildElement = false,
-  isParentToggled = true
-}) => {
-  const [isToggled, setIsToggled] = React.useState(toggled);
-  const isDataArray = Array.isArray(data);
+  expandable,
+  // eslint-disable-next-line no-unused-vars
+  onToggle,
+  ...props
+}: TreeViewProps) => {
+  const [expanded, setExpanded] = useState<string[]>([]);
 
-  return (
-    <div
-      className={`tree-element ${isParentToggled && 'collapsed'} ${
-        isChildElement && 'is-child'
-      }`}
-    >
-      <span
-        className={isToggled ? 'toggler' : 'toggler closed'}
-        onClick={() => setIsToggled(!isToggled)}
-      />
-      {name ? <strong>&nbsp;&nbsp;{name}: </strong> : <span>&nbsp;&nbsp;</span>}
-      {isDataArray ? '[' : '{'}
-      {!isToggled && '...'}
-      {Object.keys(data).map((v, i, a) =>
-        typeof data[v] === 'object' ? (
-          <TreeView
-            key={`${name}-${v}-${i}`}
-            data={data[v]}
-            isLast={i === a.length - 1}
-            name={isDataArray ? null : v}
-            isChildElement
-            isParentToggled={isParentToggled && isToggled}
-          />
-        ) : (
-          <p
-            key={`${name}-${v}-${i}`}
-            className={isToggled ? 'tree-element' : 'tree-element collapsed'}
-          >
-            {isDataArray ? '' : <strong>{v}: </strong>}
-            {data[v]}
-            {i === a.length - 1 ? '' : ','}
-          </p>
-        )
-      )}
-      {isDataArray ? ']' : '}'}
-      {!isLast ? ',' : ''}
-    </div>
-  );
-};
+  const handleToggle = (value: string) => {
+    const currentIndex = expanded.indexOf(value);
```

### usePersistedState (task/45)

#### canonical solution

```javascript
const usePersistedState = (name, defaultValue) => {
  const [value, setValue] = React.useState(defaultValue);
  const nameRef = React.useRef(name);

  React.useEffect(() => {
    try {
      const storedValue = localStorage.getItem(name);
      if (storedValue !== null) setValue(storedValue);
      else localStorage.setItem(name, defaultValue);
    } catch {
      setValue(defaultValue);
    }
  }, []);

  React.useEffect(() => {
    try {
      localStorage.setItem(nameRef.current, value);
    } catch {}
  }, [value]);

  React.useEffect(() => {
    const lastName = nameRef.current;
    if (name !== lastName) {
      try {
        localStorage.setItem(name, value);
        nameRef.current = name;
        localStorage.removeItem(lastName);
      } catch {}
    }
  }, [name]);

  return [value, setValue];
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,33 +1,14 @@

 const usePersistedState = (name, defaultValue) => {
-  const [value, setValue] = React.useState(defaultValue);
-  const nameRef = React.useRef(name);
+  const [value, setValue] = useState(() => {
+    const persistedValue = JSON.parse(
+      localStorage.getItem(name) || String(defaultValue)
+    );
+    return persistedValue;
+  });
 
-  React.useEffect(() => {
-    try {
-      const storedValue = localStorage.getItem(name);
-      if (storedValue !== null) setValue(storedValue);
-      else localStorage.setItem(name, defaultValue);
-    } catch {
-      setValue(defaultValue);
-    }
-  }, []);
+  const setValuePersisted = (value) => {
+    setValue(value);
+    localStorage.setItem(name, JSON.stringify(value));
+  };
 
-  React.useEffect(() => {
-    try {
-      localStorage.setItem(nameRef.current, value);
-    } catch {}
-  }, [value]);
-
-  React.useEffect(() => {
-    const lastName = nameRef.current;
-    if (name !== lastName) {
-      try {
-        localStorage.setItem(name, value);
-        nameRef.current = name;
-        localStorage.removeItem(lastName);
-      } catch {}
-    }
-  }, [name]);
-
-  return [value, setValue];
-};
+  return [value
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,33 +1,13 @@

 const usePersistedState = (name, defaultValue) => {
-  const [value, setValue] = React.useState(defaultValue);
-  const nameRef = React.useRef(name);
+  const [value, setValue] = useState(() => {
+    const persistedValue = localStorage.getItem(name);
+    return persistedValue === null ? defaultValue : persistedValue;
+  });
 
-  React.useEffect(() => {
-    try {
-      const storedValue = localStorage.getItem(name);
-      if (storedValue !== null) setValue(storedValue);
-      else localStorage.setItem(name, defaultValue);
-    } catch {
-      setValue(defaultValue);
-    }
+  const setValuePersisted = useCallback(value => {
+    setValue(value);
+    localStorage.setItem(name, value);
   }, []);
 
-  React.useEffect(() => {
-    try {
-      localStorage.setItem(nameRef.current, value);
-    } catch {}
-  }, [value]);
-
-  React.useEffect(() => {
-    const lastName = nameRef.current;
-    if (name !== lastName) {
-      try {
-        localStorage.setItem(name, value);
-        nameRef.current = name;
-        localStorage.removeItem(lastName);
-      } catch {}
-    }
-  }, [name]);
-
-  return [value, setValue];
+  return [value, setValuePersisted];
 };
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,33 +1,13 @@

 const usePersistedState = (name, defaultValue) => {
-  const [value, setValue] = React.useState(defaultValue);
-  const nameRef = React.useRef(name);
+  const store = getOrCreateStore();
+  const [state, setState] = useState(() => store.get(name, defaultValue));
 
-  React.useEffect(() => {
-    try {
-      const storedValue = localStorage.getItem(name);
-      if (storedValue !== null) setValue(storedValue);
-      else localStorage.setItem(name, defaultValue);
-    } catch {
-      setValue(defaultValue);
-    }
-  }, []);
+  const setPersistedState = value => {
+    setState(value);
+    store.set(name, value);
+  };
 
-  React.useEffect(() => {
-    try {
-      localStorage.setItem(nameRef.current, value);
-    } catch {}
-  }, [value]);
+  return [state, setPersistedState];
+};
 
-  React.useEffect(() => {
-    const lastName = nameRef.current;
-    if (name !== lastName) {
-      try {
-        localStorage.setItem(name, value);
-        nameRef.current = name;
-        localStorage.removeItem(lastName);
-      } catch {}
-    }
-  }, [name]);
-
-  return [value, setValue];
-};
+export default usePersistedState;
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,33 +1,10 @@

 const usePersistedState = (name, defaultValue) => {
-  const [value, setValue] = React.useState(defaultValue);
-  const nameRef = React.useRef(name);
+  const [state, setState] = useState(() => {
+    const persistedState = window.localStorage.getItem(name);
+    return persistedState ? JSON.parse(persistedState) : defaultValue;
+  });
 
-  React.useEffect(() => {
-    try {
-      const storedValue = localStorage.getItem(name);
-      if (storedValue !== null) setValue(storedValue);
-      else localStorage.setItem(name, defaultValue);
-    } catch {
-      setValue(defaultValue);
-    }
-  }, []);
-
-  React.useEffect(() => {
-    try {
-      localStorage.setItem(nameRef.current, value);
-    } catch {}
-  }, [value]);
-
-  React.useEffect(() => {
-    const lastName = nameRef.current;
-    if (name !== lastName) {
-      try {
-        localStorage.setItem(name, value);
-        nameRef.current = name;
-        localStorage.removeItem(lastName);
-      } catch {}
-    }
-  }, [name]);
-
-  return [value, setValue];
-};
+  const setStateAndPersist = (newState) => {
+    setState(newState);
+    window.localStorage.setItem(name, JSON.stringify(newState));
+  };
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,33 +1,13 @@

 const usePersistedState = (name, defaultValue) => {
-  const [value, setValue] = React.useState(defaultValue);
-  const nameRef = React.useRef(name);
+  const [state, setState] = useState(() => {
+    const nameFromStorage = window.localStorage.getItem(name);
+    if (nameFromStorage) {
+      return JSON.parse(nameFromStorage);
+    }
+    return defaultValue;
+  });
 
-  React.useEffect(() => {
-    try {
-      const storedValue = localStorage.getItem(name);
-      if (storedValue !== null) setValue(storedValue);
-      else localStorage.setItem(name, defaultValue);
-    } catch {
-      setValue(defaultValue);
-    }
-  }, []);
-
-  React.useEffect(() => {
-    try {
-      localStorage.setItem(nameRef.current, value);
-    } catch {}
-  }, [value]);
-
-  React.useEffect(() => {
-    const lastName = nameRef.current;
-    if (name !== lastName) {
-      try {
-        localStorage.setItem(name, value);
-        nameRef.current = name;
-        localStorage.removeItem(lastName);
-      } catch {}
-    }
-  }, [name]);
-
-  return [value, setValue];
-};
+  const setStateToStorage = useCallback(
+    value => {
+      setState(value);
+      window.localStorage.setItem(name
```

### useWindowSize (task/46)

#### canonical solution

```javascript
const useWindowSize = () => {
  const [windowSize, setWindowSize] = React.useState({
    width: undefined,
    height: undefined,
  });

  React.useEffect(() => {
    const handleResize = () =>
      setWindowSize({ width: window.innerWidth, height: window.innerHeight });

    window.addEventListener('resize', handleResize);

    handleResize();

    return () => {
      window.removeEventListener('resize', handleResize);
    };
  }, []);

  return windowSize;
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,21 +1,17 @@

 const useWindowSize = () => {
-  const [windowSize, setWindowSize] = React.useState({
-    width: undefined,
-    height: undefined,
-  });
+    const [size, setSize] = useState({
+        width: window.innerWidth,
+        height: window.innerHeight
+    });
 
-  React.useEffect(() => {
-    const handleResize = () =>
-      setWindowSize({ width: window.innerWidth, height: window.innerHeight });
+    useEffect(() => {
+        const handleResize = () => {
+            setSize({
+                width: window.innerWidth,
+                height: window.innerHeight
+            });
+        };
 
-    window.addEventListener('resize', handleResize);
+        window.addEventListener('resize', handleResize);
 
-    handleResize();
-
-    return () => {
-      window.removeEventListener('resize', handleResize);
-    };
-  }, []);
-
-  return windowSize;
-};
+        return () =>
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,21 +1,17 @@

 const useWindowSize = () => {
-  const [windowSize, setWindowSize] = React.useState({
-    width: undefined,
-    height: undefined,
+  const [size, setSize] = useState({
+    width: window.innerWidth,
+    height: window.innerHeight,
   });
 
-  React.useEffect(() => {
-    const handleResize = () =>
-      setWindowSize({ width: window.innerWidth, height: window.innerHeight });
+  useEffect(() => {
+    const onResize = () => {
+      setSize({
+        width: window.innerWidth,
+        height: window.innerHeight,
+      });
+    };
 
-    window.addEventListener('resize', handleResize);
+    window.addEventListener('resize', onResize);
 
-    handleResize();
-
-    return () => {
-      window.removeEventListener('resize', handleResize);
-    };
-  }, []);
-
-  return windowSize;
-};
+    return
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,21 +1,15 @@

 const useWindowSize = () => {
-  const [windowSize, setWindowSize] = React.useState({
-    width: undefined,
-    height: undefined,
+  const [windowSize, setWindowSize] = useState({
+    width: window.innerWidth,
+    height: window.innerHeight,
   });
 
-  React.useEffect(() => {
-    const handleResize = () =>
-      setWindowSize({ width: window.innerWidth, height: window.innerHeight });
+  useEffect(() => {
+    const handleResize = () => {
+      setWindowSize({
+        width: window.innerWidth,
+        height: window.innerHeight,
+      });
+    };
 
     window.addEventListener('resize', handleResize);
-
-    handleResize();
-
-    return () => {
-      window.removeEventListener('resize', handleResize);
-    };
-  }, []);
-
-  return windowSize;
-};
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,21 +1,16 @@

 const useWindowSize = () => {
-  const [windowSize, setWindowSize] = React.useState({
-    width: undefined,
-    height: undefined,
+  const [size, setSize] = useState({
+    width: window.innerWidth,
+    height: window.innerHeight,
   });
 
-  React.useEffect(() => {
-    const handleResize = () =>
-      setWindowSize({ width: window.innerWidth, height: window.innerHeight });
+  useEffect(() => {
+    const handleResize = () => {
+      setSize({
+        width: window.innerWidth,
+        height: window.innerHeight,
+      });
+    };
 
     window.addEventListener('resize', handleResize);
-
-    handleResize();
-
-    return () => {
-      window.removeEventListener('resize', handleResize);
-    };
-  }, []);
-
-  return windowSize;
-};
+    return
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,21 +1,16 @@

 const useWindowSize = () => {
-  const [windowSize, setWindowSize] = React.useState({
-    width: undefined,
-    height: undefined,
+  const [windowSize, setWindowSize] = useState({
+    width: window.innerWidth,
+    height: window.innerHeight,
   });
 
-  React.useEffect(() => {
-    const handleResize = () =>
-      setWindowSize({ width: window.innerWidth, height: window.innerHeight });
+  useEffect(() => {
+    function handleResize() {
+      setWindowSize({
+        width: window.innerWidth,
+        height: window.innerHeight,
+      });
+    }
 
-    window.addEventListener('resize', handleResize);
-
-    handleResize();
-
-    return () => {
-      window.removeEventListener('resize', handleResize);
-    };
-  }, []);
-
-  return windowSize;
-};
+    window.addEventListener("resize", handleResize);
+   
```

### ControlledInput (task/47)

#### canonical solution

```javascript
const ControlledInput = ({ value, onValueChange, ...rest }) => {
  return (
    <input
      value={value}
      onChange={({ target: { value } }) => onValueChange(value)}
      {...rest}
    />
  );
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,9 +1,11 @@

 const ControlledInput = ({ value, onValueChange, ...rest }) => {
   return (
-    <input
+    <Input
       value={value}
-      onChange={({ target: { value } }) => onValueChange(value)}
+      onChange={(event) => onValueChange(event.target.value)}
       {...rest}
     />
   );
 };
+
+export default ControlledInput;
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,9 +1,14 @@

 const ControlledInput = ({ value, onValueChange, ...rest }) => {
-  return (
-    <input
-      value={value}
-      onChange={({ target: { value } }) => onValueChange(value)}
-      {...rest}
-    />
+  const handleChange = useCallback(
+    e => {
+      onValueChange(e.target.value);
+    },
+    [onValueChange]
   );
+
+  return <input value={value} onChange={handleChange} {...rest} />;
 };
+
+ControlledInput.propTypes = {
+  value: PropTypes.string.isRequired,
+  onValueChange: PropTypes.func.isRequired
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,9 +1,14 @@

 const ControlledInput = ({ value, onValueChange, ...rest }) => {
-  return (
-    <input
-      value={value}
-      onChange={({ target: { value } }) => onValueChange(value)}
-      {...rest}
-    />
+  const [controlledValue, setControlledValue] = useState(value);
+
+  const onChange = useCallback(
+    (event) => {
+      setControlledValue(event.target.value);
+      onValueChange(event.target.value);
+    },
+    [onValueChange],
   );
-};
+
+  useEffect(() => {
+    setControlledValue(value);
+  }, [value]);
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,9 +1,14 @@

 const ControlledInput = ({ value, onValueChange, ...rest }) => {
+  const handleChange = e => {
+    const value = e.target.value;
+    onValueChange(value);
+  };
+
   return (
-    <input
-      value={value}
-      onChange={({ target: { value } }) => onValueChange(value)}
-      {...rest}
-    />
-  );
-};
+    <div>
+      <input
+        onChange={handleChange}
+        value={value}
+        {...rest}
+      />
+    </div>
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,9 +1,14 @@

 const ControlledInput = ({ value, onValueChange, ...rest }) => {
+  const handleChange = (e) => {
+    if (rest.type === 'number') {
+      onValueChange(parseInt(e.target.value, 10));
+    } else {
+      onValueChange(e.target.value);
+    }
+  };
+
   return (
     <input
+      type={rest.type}
       value={value}
-      onChange={({ target: { value } }) => onValueChange(value)}
-      {...rest}
-    />
-  );
-};
+      onChange={handleChange}
```

### DataTable (task/48)

#### canonical solution

```javascript
const DataTable = ({ data }) => {
  return (
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Value</th>
        </tr>
      </thead>
      <tbody>
        {data.map((val, i) => (
          <tr key={`${i}_${val}`}>
            <td>{i}</td>
            <td>{val}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,20 +1,13 @@

 const DataTable = ({ data }) => {
   return (
-    <table>
-      <thead>
-        <tr>
-          <th>ID</th>
-          <th>Value</th>
-        </tr>
-      </thead>
-      <tbody>
-        {data.map((val, i) => (
-          <tr key={`${i}_${val}`}>
-            <td>{i}</td>
-            <td>{val}</td>
+    <div className="table-container">
+      <table className="table table-striped table-bordered">
+        <thead>
+          <tr>
+            <th>Date</th>
+            <th>Description</th>
+            <th>Credit</th>
+            <th>Debit</th>
+            <th>Balance</th>
           </tr>
-        ))}
-      </tbody>
-    </table>
-  );
-};
+        </thead
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,20 +1,14 @@

 const DataTable = ({ data }) => {
   return (
-    <table>
+    <table className="table table-hover">
       <thead>
         <tr>
-          <th>ID</th>
-          <th>Value</th>
+          <th>Name</th>
+          <th>Email</th>
+          <th>Description</th>
+          <th>Status</th>
+          <th>Created At</th>
+          <th>Updated At</th>
         </tr>
       </thead>
-      <tbody>
-        {data.map((val, i) => (
-          <tr key={`${i}_${val}`}>
-            <td>{i}</td>
-            <td>{val}</td>
-          </tr>
-        ))}
-      </tbody>
-    </table>
-  );
-};
+      <tbody
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,20 +1,20 @@

 const DataTable = ({ data }) => {
+  const columns = React.useMemo(
+    () => [
+      {
+        Header: 'Name',
+        accessor: 'name',
+      },
+      {
+        Header: 'Info',
+        accessor: 'info',
+      },
+    ],
+    []
+  );
+
   return (
-    <table>
-      <thead>
-        <tr>
-          <th>ID</th>
-          <th>Value</th>
-        </tr>
-      </thead>
-      <tbody>
-        {data.map((val, i) => (
-          <tr key={`${i}_${val}`}>
-            <td>{i}</td>
-            <td>{val}</td>
-          </tr>
-        ))}
-      </tbody>
-    </table>
-  );
-};
+    <ReactTable
+      data={data}
+      columns={columns}
+      defaultPageSize={10}
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,20 +1,13 @@

 const DataTable = ({ data }) => {
+  const dataRows = data.map((row, i) => (
+    <tr key={i}>
+      {Object.keys(row).map((key, i) => (
+        <td key={i}>{row[key]}</td>
+      ))}
+    </tr>
+  ));
+
   return (
-    <table>
+    <Table className="custom-table">
       <thead>
         <tr>
-          <th>ID</th>
-          <th>Value</th>
-        </tr>
-      </thead>
-      <tbody>
-        {data.map((val, i) => (
-          <tr key={`${i}_${val}`}>
-            <td>{i}</td>
-            <td>{val}</td>
-          </tr>
-        ))}
-      </tbody>
-    </table>
-  );
-};
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,20 +1,12 @@

 const DataTable = ({ data }) => {
   return (
-    <table>
-      <thead>
-        <tr>
-          <th>ID</th>
-          <th>Value</th>
-        </tr>
-      </thead>
-      <tbody>
-        {data.map((val, i) => (
-          <tr key={`${i}_${val}`}>
-            <td>{i}</td>
-            <td>{val}</td>
-          </tr>
-        ))}
-      </tbody>
-    </table>
-  );
-};
+    <TableContainer>
+      <Table aria-label="simple table">
+        <TableHead>
+          <TableRow>
+            <TableCell align="left">Date</TableCell>
+            <TableCell align="left">Description</TableCell>
+            <TableCell align="left">Category</TableCell>
+            <TableCell align="left">Amount</TableCell>
+          </TableRow>
+        </
```

### useComponentWillUnmount (task/49)

#### canonical solution

```javascript
const useComponentWillUnmount = onUnmountHandler => {
  React.useEffect(
    () => () => {
      onUnmountHandler();
    },
    []
  );
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,8 +1,9 @@

 const useComponentWillUnmount = onUnmountHandler => {
-  React.useEffect(
-    () => () => {
-      onUnmountHandler();
-    },
-    []
-  );
-};
+  const componentWillUnmount = () => {
+    onUnmountHandler()
+  }
+
+  return [componentWillUnmount]
+}
+
+export default useComponentWillUnmount
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,8 +1,13 @@

 const useComponentWillUnmount = onUnmountHandler => {
-  React.useEffect(
-    () => () => {
+  useEffect(() => {
+    return () => {
       onUnmountHandler();
-    },
-    []
-  );
+    };
+  }, []);
 };
+
+const useComponentDidMount = onMountHandler => {
+  useEffect(() => {
+    onMountHandler();
+  }, []);
+};
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,8 +1,11 @@

 const useComponentWillUnmount = onUnmountHandler => {
-  React.useEffect(
-    () => () => {
-      onUnmountHandler();
-    },
-    []
-  );
+  const componentWillUnmount = props => {
+    if (onUnmountHandler) {
+      onUnmountHandler(props);
+    }
+  };
+
+  return [componentWillUnmount];
 };
+
+export default useComponentWillUnmount;
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,8 +1,12 @@

 const useComponentWillUnmount = onUnmountHandler => {
-  React.useEffect(
-    () => () => {
-      onUnmountHandler();
-    },
-    []
-  );
-};
+  const previousComponentWillUnmount =
+    React.Component.prototype.componentWillUnmount;
+
+  React.Component.prototype.componentWillUnmount = function() {
+    if (typeof previousComponentWillUnmount === 'function') {
+      previousComponentWillUnmount.call(this);
+    }
+
+    if (typeof onUnmountHandler === 'function') {
+      onUnmountHandler.call(this);
+    }
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,8 +1,13 @@

 const useComponentWillUnmount = onUnmountHandler => {
-  React.useEffect(
-    () => () => {
-      onUnmountHandler();
-    },
-    []
-  );
-};
+  const prevUnmount = useRef();
+  const prevUnmountSet = useRef(false);
+
+  useEffect(() => {
+    prevUnmount.current = onUnmountHandler;
+    prevUnmountSet.current = true;
+  }, [onUnmountHandler]);
+
+  useEffect(() => {
+    if (prevUnmountSet.current) {
+      prevUnmount.current();
+    }
```

### Tabs (task/50)

#### canonical solution

```javascript
const TabItem = props => <div {...props} />;

const Tabs = ({ defaultIndex = 0, onTabClick, children }) => {
  const [bindIndex, setBindIndex] = React.useState(defaultIndex);
  const changeTab = newIndex => {
    if (typeof onTabClick === 'function') onTabClick(newIndex);
    setBindIndex(newIndex);
  };
  const items = children.filter(item => item.type.name === 'TabItem');

  return (
    <div className="wrapper">
      <div className="tab-menu">
        {items.map(({ props: { index, label } }) => (
          <button
            key={`tab-btn-${index}`}
            onClick={() => changeTab(index)}
            className={bindIndex === index ? 'focus' : ''}
          >
            {label}
          </button>
        ))}
      </div>
      <div className="tab-view">
        {items.map(({ props }) => (
          <div
            {...props}
            className={`tab-content ${
              bindIndex === props.index ? 'selected' : ''
            }`}
            key={`tab-content-${props.index}`}
          />
        ))}
      </div>
    </div>
  );
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,37 +1,15 @@

 const TabItem = props => <div {...props} />;
 
 const Tabs = ({ defaultIndex = 0, onTabClick, children }) => {
-  const [bindIndex, setBindIndex] = React.useState(defaultIndex);
-  const changeTab = newIndex => {
-    if (typeof onTabClick === 'function') onTabClick(newIndex);
-    setBindIndex(newIndex);
+  const [activeIndex, setActiveIndex] = useState(defaultIndex);
+
+  const handleTabClick = index => {
+    setActiveIndex(index);
+    onTabClick && onTabClick(index);
   };
-  const items = children.filter(item => item.type.name === 'TabItem');
 
   return (
-    <div className="wrapper">
-      <div className="tab-menu">
-        {items.map(({ props: { index, label } }) => (
-          <button
-            key={`tab-btn-${index}`}
-            onClick={() => changeTab(index)}
-            className={bindIndex === index ? 'focus' : ''}
-          >
-            {label}
-          </button>
-        ))}
-      </div>
-      <div className="tab-view">
-        {items.map(({ props }) => (
-          <div
-            {...props}
-            className={`tab-content ${
-              bindIndex === props.index ? 'selected' : ''
-            }`}
-            key={`tab-content-${props.index}`}
-          />
-        ))}
-      </div>
-    </div>
-  );
-};
+    <ul className="tabs">
+      {React.Children.map(children, (child, index) => {
+        const { disabled } = child.props;
+        const
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,37 +1,15 @@

 const TabItem = props => <div {...props} />;
 
 const Tabs = ({ defaultIndex = 0, onTabClick, children }) => {
-  const [bindIndex, setBindIndex] = React.useState(defaultIndex);
-  const changeTab = newIndex => {
-    if (typeof onTabClick === 'function') onTabClick(newIndex);
-    setBindIndex(newIndex);
+  const [currentIndex, setCurrentIndex] = useState(defaultIndex);
+
+  const onClick = index => {
+    setCurrentIndex(index);
+    onTabClick && onTabClick(index);
   };
-  const items = children.filter(item => item.type.name === 'TabItem');
 
   return (
-    <div className="wrapper">
-      <div className="tab-menu">
-        {items.map(({ props: { index, label } }) => (
-          <button
-            key={`tab-btn-${index}`}
-            onClick={() => changeTab(index)}
-            className={bindIndex === index ? 'focus' : ''}
-          >
-            {label}
-          </button>
-        ))}
-      </div>
-      <div className="tab-view">
-        {items.map(({ props }) => (
-          <div
-            {...props}
-            className={`tab-content ${
-              bindIndex === props.index ? 'selected' : ''
-            }`}
-            key={`tab-content-${props.index}`}
-          />
-        ))}
-      </div>
-    </div>
-  );
-};
+    <div className="tabs">
+      <ul className="tabs-nav">
+        {React.Children.map(children, (child, index) => {
+          return (
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,37 +1,15 @@

 const TabItem = props => <div {...props} />;
 
 const Tabs = ({ defaultIndex = 0, onTabClick, children }) => {
-  const [bindIndex, setBindIndex] = React.useState(defaultIndex);
-  const changeTab = newIndex => {
-    if (typeof onTabClick === 'function') onTabClick(newIndex);
-    setBindIndex(newIndex);
+  const [currentIndex, setCurrentIndex] = useState(defaultIndex);
+
+  const handleTabClick = index => {
+    setCurrentIndex(index);
+    onTabClick && onTabClick(index);
   };
-  const items = children.filter(item => item.type.name === 'TabItem');
 
   return (
-    <div className="wrapper">
-      <div className="tab-menu">
-        {items.map(({ props: { index, label } }) => (
-          <button
-            key={`tab-btn-${index}`}
-            onClick={() => changeTab(index)}
-            className={bindIndex === index ? 'focus' : ''}
-          >
-            {label}
-          </button>
-        ))}
-      </div>
-      <div className="tab-view">
-        {items.map(({ props }) => (
-          <div
-            {...props}
-            className={`tab-content ${
-              bindIndex === props.index ? 'selected' : ''
-            }`}
-            key={`tab-content-${props.index}`}
-          />
-        ))}
-      </div>
-    </div>
-  );
-};
+    <ul className="c-tabs">
+      {React.Children.map(children, (child, index) => {
+        if (!child) {
+          return null;
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,37 +1,15 @@

 const TabItem = props => <div {...props} />;
 
 const Tabs = ({ defaultIndex = 0, onTabClick, children }) => {
-  const [bindIndex, setBindIndex] = React.useState(defaultIndex);
-  const changeTab = newIndex => {
-    if (typeof onTabClick === 'function') onTabClick(newIndex);
-    setBindIndex(newIndex);
+  const [activeIndex, setActiveIndex] = useState(defaultIndex);
+
+  const onClick = (index, disabled) => {
+    if (!disabled) {
+      setActiveIndex(index);
+      onTabClick && onTabClick(index);
+    }
   };
-  const items = children.filter(item => item.type.name === 'TabItem');
 
   return (
-    <div className="wrapper">
-      <div className="tab-menu">
-        {items.map(({ props: { index, label } }) => (
-          <button
-            key={`tab-btn-${index}`}
-            onClick={() => changeTab(index)}
-            className={bindIndex === index ? 'focus' : ''}
-          >
-            {label}
-          </button>
-        ))}
-      </div>
-      <div className="tab-view">
-        {items.map(({ props }) => (
-          <div
-            {...props}
-            className={`tab-content ${
-              bindIndex === props.index ? 'selected' : ''
-            }`}
-            key={`tab-content-${props.index}`}
-          />
-        ))}
-      </div>
-    </div>
-  );
-};
+    <div className="tabs">
+      <TabItem onClick={() => onClick(0, children[0].props
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,37 +1,15 @@

 const TabItem = props => <div {...props} />;
 
 const Tabs = ({ defaultIndex = 0, onTabClick, children }) => {
-  const [bindIndex, setBindIndex] = React.useState(defaultIndex);
-  const changeTab = newIndex => {
-    if (typeof onTabClick === 'function') onTabClick(newIndex);
-    setBindIndex(newIndex);
+  const [currentIndex, setCurrentIndex] = useState(defaultIndex);
+
+  const handleTabClick = index => {
+    setCurrentIndex(index);
+    onTabClick && onTabClick(index);
   };
-  const items = children.filter(item => item.type.name === 'TabItem');
 
   return (
-    <div className="wrapper">
-      <div className="tab-menu">
-        {items.map(({ props: { index, label } }) => (
-          <button
-            key={`tab-btn-${index}`}
-            onClick={() => changeTab(index)}
-            className={bindIndex === index ? 'focus' : ''}
-          >
-            {label}
-          </button>
-        ))}
-      </div>
-      <div className="tab-view">
-        {items.map(({ props }) => (
-          <div
-            {...props}
-            className={`tab-content ${
-              bindIndex === props.index ? 'selected' : ''
-            }`}
-            key={`tab-content-${props.index}`}
-          />
-        ))}
-      </div>
-    </div>
-  );
-};
+    <div className="tabs">
+      <div className="tabs-nav">
+        {React.Children.map(children, (child, index) => {
+          const
```

### useNavigatorOnLine (task/51)

#### canonical solution

```javascript
const getOnLineStatus = () =>
  typeof navigator !== 'undefined' && typeof navigator.onLine === 'boolean'
    ? navigator.onLine
    : true;

const useNavigatorOnLine = () => {
  const [status, setStatus] = React.useState(getOnLineStatus());

  const setOnline = () => setStatus(true);
  const setOffline = () => setStatus(false);

  React.useEffect(() => {
    window.addEventListener('online', setOnline);
    window.addEventListener('offline', setOffline);

    return () => {
      window.removeEventListener('online', setOnline);
      window.removeEventListener('offline', setOffline);
    };
  }, []);

  return status;
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,22 +1,14 @@

-const getOnLineStatus = () =>  typeof navigator !== 'undefined' && typeof navigator.onLine === 'boolean'
-    ? navigator.onLine
-    : true;
+const getOnLineStatus = () => {
+  return typeof navigator !== 'undefined' ? navigator.onLine : true;
+};
 
-const useNavigatorOnLine = () => {
-  const [status, setStatus] = React.useState(getOnLineStatus());
+export default function networkStatus(): Observable<boolean> {
+  return new Observable(subscriber => {
+    const onlineStatus = getOnLineStatus();
+    subscriber.next(onlineStatus);
 
-  const setOnline = () => setStatus(true);
-  const setOffline = () => setStatus(false);
+    const handler = () => {
+      subscriber.next(getOnLineStatus());
+    };
 
-  React.useEffect(() => {
-    window.addEventListener('online', setOnline);
-    window.addEventListener('offline', setOffline);
-
-    return () => {
-      window.removeEventListener('online', setOnline);
-      window.removeEventListener('offline', setOffline);
-    };
-  }, []);
-
-  return status;
-};
+    const eventHandler =
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,22 +1,19 @@

-const getOnLineStatus = () =>  typeof navigator !== 'undefined' && typeof navigator.onLine === 'boolean'
-    ? navigator.onLine
-    : true;
+const getOnLineStatus = () => {
+  return {
+    type: GET_ONLINE_STATUS,
+    online: online
+  };
+};
 
-const useNavigatorOnLine = () => {
-  const [status, setStatus] = React.useState(getOnLineStatus());
+export const getOnlineStatus = () => {
+  if (isBrowser) {
+    const status = navigator.onLine;
+    setOnline(status);
+    return status;
+  }
+  return online;
+};
 
-  const setOnline = () => setStatus(true);
-  const setOffline = () => setStatus(false);
-
-  React.useEffect(() => {
-    window.addEventListener('online', setOnline);
-    window.addEventListener('offline', setOffline);
-
-    return () => {
-      window.removeEventListener('online', setOnline);
-      window.removeEventListener('offline', setOffline);
-    };
-  }, []);
-
-  return status;
-};
+export const setOnline = status => {
+  online = status;
+  if (is
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,22 +1,16 @@

-const getOnLineStatus = () =>  typeof navigator !== 'undefined' && typeof navigator.onLine === 'boolean'
-    ? navigator.onLine
-    : true;
+const getOnLineStatus = () => {
+  const { app } = window.webviewApis;
+  if (app) {
+    return app.getOnLineStatus();
+  }
+  return false;
+};
 
-const useNavigatorOnLine = () => {
-  const [status, setStatus] = React.useState(getOnLineStatus());
+const updateOnLineStatus = (status: boolean) => {
+  const { app } = window.webviewApis;
+  if (app) {
+    app.updateOnLineStatus(status);
+  }
+};
 
-  const setOnline = () => setStatus(true);
-  const setOffline = () => setStatus(false);
-
-  React.useEffect(() => {
-    window.addEventListener('online', setOnline);
-    window.addEventListener('offline', setOffline);
-
-    return () => {
-      window.removeEventListener('online', setOnline);
-      window.removeEventListener('offline', setOffline);
-    };
-  }, []);
-
-  return status;
-};
+// getCurrentUrl
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,22 +1,20 @@

-const getOnLineStatus = () =>  typeof navigator !== 'undefined' && typeof navigator.onLine === 'boolean'
-    ? navigator.onLine
-    : true;
+const getOnLineStatus = () => {
+  return {
+    type: GET_ONLINE_STATUS,
+    onLineStatus: true
+  };
+};
 
-const useNavigatorOnLine = () => {
-  const [status, setStatus] = React.useState(getOnLineStatus());
+export const offLineStatus = () => {
+  return {
+    type: OFF_LINE_STATUS,
+    onLineStatus: false
+  };
+};
 
-  const setOnline = () => setStatus(true);
-  const setOffline = () => setStatus(false);
+export const removeUserInfo = () => {
+  return {
+    type: REMOVE_USER_INFO
+  };
+};
 
-  React.useEffect(() => {
-    window.addEventListener('online', setOnline);
-    window.addEventListener('offline', setOffline);
-
-    return () => {
-      window.removeEventListener('online', setOnline);
-      window.removeEventListener('offline', setOffline);
-    };
-  }, []);
-
-  return status;
-};
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,22 +1,7 @@

-const getOnLineStatus = () =>  typeof navigator !== 'undefined' && typeof navigator.onLine === 'boolean'
-    ? navigator.onLine
-    : true;
-
-const useNavigatorOnLine = () => {
-  const [status, setStatus] = React.useState(getOnLineStatus());
-
-  const setOnline = () => setStatus(true);
-  const setOffline = () => setStatus(false);
-
-  React.useEffect(() => {
-    window.addEventListener('online', setOnline);
-    window.addEventListener('offline', setOffline);
-
-    return () => {
-      window.removeEventListener('online', setOnline);
-      window.removeEventListener('offline', setOffline);
-    };
-  }, []);
-
-  return status;
-};
+const getOnLineStatus = () => {
+  return (dispatch: Dispatch<ActionTypes>) => {
+    axios.get('https://www.easy-mock.com/mock/5c8a3a14ac2acb3a322b28f5/example/onlineStatus')
+      .then((res) => {
+        if (res.data.code === 0) {
+          dispatch(changeOnLineStatus(res.data.data));
+        }
```

### PasswordRevealer (task/52)

#### canonical solution

```javascript
const PasswordRevealer = ({ value }) => {
  const [shown, setShown] = React.useState(false);
  return (
    <>
      <input type={shown ? 'text' : 'password'} value={value} />
      <button onClick={() => setShown(!shown)}>Show/Hide</button>
    </>
  );
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,9 +1,14 @@

 const PasswordRevealer = ({ value }) => {
-  const [shown, setShown] = React.useState(false);
+  const [visible, setVisible] = useState(false);
+
+  const handleToggleVisible = () => {
+    setVisible(!visible);
+  };
+
   return (
     <>
-      <input type={shown ? 'text' : 'password'} value={value} />
-      <button onClick={() => setShown(!shown)}>Show/Hide</button>
-    </>
-  );
-};
+      <Input
+        type={visible ? 'text' : 'password'}
+        value={value}
+        endAdornment={
+          <InputAdornment position="end">
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,9 +1,13 @@

 const PasswordRevealer = ({ value }) => {
-  const [shown, setShown] = React.useState(false);
+  const [showPassword, setShowPassword] = useState(false);
+
+  const toggleShowPassword = () => {
+    setShowPassword(!showPassword);
+  };
+
   return (
-    <>
-      <input type={shown ? 'text' : 'password'} value={value} />
-      <button onClick={() => setShown(!shown)}>Show/Hide</button>
-    </>
-  );
-};
+    <div className="relative">
+      <input
+        type={showPassword ? 'text' : 'password'}
+        value={value}
+        className="w-full px-3 py-2 rounded-md text-sm
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,9 +1,12 @@

 const PasswordRevealer = ({ value }) => {
-  const [shown, setShown] = React.useState(false);
+  const [isRevealed, setIsRevealed] = useState(false);
+
   return (
-    <>
-      <input type={shown ? 'text' : 'password'} value={value} />
-      <button onClick={() => setShown(!shown)}>Show/Hide</button>
-    </>
+    <div className="py-2 px-4">
+      <RevealPassword
+        value={value}
+        isRevealed={isRevealed}
+        onToggleReveal={() => setIsRevealed(!isRevealed)}
+      />
+    </div>
   );
-};
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,9 +1,12 @@

 const PasswordRevealer = ({ value }) => {
-  const [shown, setShown] = React.useState(false);
+  const [isRevealed, setIsRevealed] = useState(false);
+
   return (
-    <>
-      <input type={shown ? 'text' : 'password'} value={value} />
-      <button onClick={() => setShown(!shown)}>Show/Hide</button>
-    </>
-  );
-};
+    <div className="password-revealer">
+      <div
+        className="password-revealer__input"
+        onClick={() => setIsRevealed(!isRevealed)}
+      >
+        {value.replace(/./g, '●')}
+      </div>
+      <Tool
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,9 +1,14 @@

 const PasswordRevealer = ({ value }) => {
-  const [shown, setShown] = React.useState(false);
+  const [visible, setVisible] = useState(false);
+
   return (
-    <>
-      <input type={shown ? 'text' : 'password'} value={value} />
-      <button onClick={() => setShown(!shown)}>Show/Hide</button>
-    </>
-  );
-};
+    <React.Fragment>
+      <Input
+        type={visible ? 'text' : 'password'}
+        value={value}
+        onChange={() => {}}
+        endAdornment={
+          <InputAdornment position="end">
+            <IconButton
+              aria-label="toggle password visibility"
+              on
```

### StarRating (task/53)

#### canonical solution

```javascript
const Star = ({ marked, starId }) => {
  return (
    <span data-star-id={starId} className="star" role="button">
      {marked ? '\u2605' : '\u2606'}
    </span>
  );
};

const StarRating = ({ value }) => {
  const [rating, setRating] = React.useState(parseInt(value) || 0);
  const [selection, setSelection] = React.useState(0);

  const hoverOver = event => {
    let val = 0;
    if (event && event.target && event.target.getAttribute('data-star-id'))
      val = event.target.getAttribute('data-star-id');
    setSelection(val);
  };
  return (
    <div
      onMouseOut={() => hoverOver(null)}
      onClick={e => setRating(e.target.getAttribute('data-star-id') || rating)}
      onMouseOver={hoverOver}
    >
      {Array.from({ length: 5 }, (v, i) => (
        <Star
          starId={i + 1}
          key={`star_${i + 1}`}
          marked={selection ? selection >= i + 1 : rating >= i + 1}
        />
      ))}
    </div>
  );
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,34 +1,14 @@

 const Star = ({ marked, starId }) => {
   return (
-    <span data-star-id={starId} className="star" role="button">
-      {marked ? '\u2605' : '\u2606'}
-    </span>
+    <button
+      className={marked ? "star-active" : "star-inactive"}
+      onClick={() => {
+        starClicked(starId);
+      }}
+    >
+      &#x2605;
+    </button>
   );
 };
 
-const StarRating = ({ value }) => {
-  const [rating, setRating] = React.useState(parseInt(value) || 0);
-  const [selection, setSelection] = React.useState(0);
-
-  const hoverOver = event => {
-    let val = 0;
-    if (event && event.target && event.target.getAttribute('data-star-id'))
-      val = event.target.getAttribute('data-star-id');
-    setSelection(val);
-  };
-  return (
-    <div
-      onMouseOut={() => hoverOver(null)}
-      onClick={e => setRating(e.target.getAttribute('data-star-id') || rating)}
-      onMouseOver={hoverOver}
-    >
-      {Array.from({ length: 5 }, (v, i) => (
-        <Star
-          starId={i + 1}
-          key={`star_${i + 1}`}
-          marked={selection ? selection >= i + 1 : rating >= i + 1}
-        />
-      ))}
-    </div>
-  );
-};
+export default Star;
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,34 +1,9 @@

 const Star = ({ marked, starId }) => {
   return (
-    <span data-star-id={starId} className="star" role="button">
-      {marked ? '\u2605' : '\u2606'}
-    </span>
+    <div className="star" onClick={() => marked(starId)}>
+      <FontAwesomeIcon icon={faStar} />
+    </div>
   );
 };
 
-const StarRating = ({ value }) => {
-  const [rating, setRating] = React.useState(parseInt(value) || 0);
-  const [selection, setSelection] = React.useState(0);
-
-  const hoverOver = event => {
-    let val = 0;
-    if (event && event.target && event.target.getAttribute('data-star-id'))
-      val = event.target.getAttribute('data-star-id');
-    setSelection(val);
-  };
-  return (
-    <div
-      onMouseOut={() => hoverOver(null)}
-      onClick={e => setRating(e.target.getAttribute('data-star-id') || rating)}
-      onMouseOver={hoverOver}
-    >
-      {Array.from({ length: 5 }, (v, i) => (
-        <Star
-          starId={i + 1}
-          key={`star_${i + 1}`}
-          marked={selection ? selection >= i + 1 : rating >= i + 1}
-        />
-      ))}
-    </div>
-  );
-};
+export default Star;
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,34 +1,6 @@

 const Star = ({ marked, starId }) => {
-  return (
-    <span data-star-id={starId} className="star" role="button">
-      {marked ? '\u2605' : '\u2606'}
-    </span>
-  );
+  const className = marked ? 'fas fa-star' : 'far fa-star';
+  return <i className={className} id={starId} />;
 };
 
-const StarRating = ({ value }) => {
-  const [rating, setRating] = React.useState(parseInt(value) || 0);
-  const [selection, setSelection] = React.useState(0);
-
-  const hoverOver = event => {
-    let val = 0;
-    if (event && event.target && event.target.getAttribute('data-star-id'))
-      val = event.target.getAttribute('data-star-id');
-    setSelection(val);
-  };
-  return (
-    <div
-      onMouseOut={() => hoverOver(null)}
-      onClick={e => setRating(e.target.getAttribute('data-star-id') || rating)}
-      onMouseOver={hoverOver}
-    >
-      {Array.from({ length: 5 }, (v, i) => (
-        <Star
-          starId={i + 1}
-          key={`star_${i + 1}`}
-          marked={selection ? selection >= i + 1 : rating >= i + 1}
-        />
-      ))}
-    </div>
-  );
-};
+export default Star;
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,34 +1,7 @@

 const Star = ({ marked, starId }) => {
-  return (
-    <span data-star-id={starId} className="star" role="button">
-      {marked ? '\u2605' : '\u2606'}
-    </span>
-  );
-};
-
-const StarRating = ({ value }) => {
-  const [rating, setRating] = React.useState(parseInt(value) || 0);
-  const [selection, setSelection] = React.useState(0);
-
-  const hoverOver = event => {
-    let val = 0;
-    if (event && event.target && event.target.getAttribute('data-star-id'))
-      val = event.target.getAttribute('data-star-id');
-    setSelection(val);
-  };
-  return (
-    <div
-      onMouseOut={() => hoverOver(null)}
-      onClick={e => setRating(e.target.getAttribute('data-star-id') || rating)}
-      onMouseOver={hoverOver}
-    >
-      {Array.from({ length: 5 }, (v, i) => (
-        <Star
-          starId={i + 1}
-          key={`star_${i + 1}`}
-          marked={selection ? selection >= i + 1 : rating >= i + 1}
-        />
-      ))}
-    </div>
-  );
-};
+  const [star, setStar] = useState(starId)
+  const [preview, setPreview] = useState(starId)
+  const [backgroundColor, setBackgroundColor] = useState('#d8e1e8')
+  const [color, setColor] = useState('#000000')
+  const [name, setName] = useState('')
+  const [description, setDescription] = useState
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,34 +1,12 @@

 const Star = ({ marked, starId }) => {
   return (
-    <span data-star-id={starId} className="star" role="button">
-      {marked ? '\u2605' : '\u2606'}
+    <span
+      onClick={() => handleStarClick(starId)}
+      className={marked ? 'Star__marked' : 'Star'}
+    >
+      *
     </span>
   );
 };
 
-const StarRating = ({ value }) => {
-  const [rating, setRating] = React.useState(parseInt(value) || 0);
-  const [selection, setSelection] = React.useState(0);
-
-  const hoverOver = event => {
-    let val = 0;
-    if (event && event.target && event.target.getAttribute('data-star-id'))
-      val = event.target.getAttribute('data-star-id');
-    setSelection(val);
-  };
-  return (
-    <div
-      onMouseOut={() => hoverOver(null)}
-      onClick={e => setRating(e.target.getAttribute('data-star-id') || rating)}
-      onMouseOver={hoverOver}
-    >
-      {Array.from({ length: 5 }, (v, i) => (
-        <Star
-          starId={i + 1}
-          key={`star_${i + 1}`}
-          marked={selection ? selection >= i + 1 : rating >= i + 1}
-        />
-      ))}
-    </div>
-  );
-};
+export default Star;
```

### useComponentDidUpdate (task/54)

#### canonical solution

```javascript
const useComponentDidUpdate = (callback, condition) => {
  const mounted = React.useRef(false);
  React.useEffect(() => {
    if (mounted.current) callback();
    else mounted.current = true;
  }, condition);
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,7 +1,12 @@

 const useComponentDidUpdate = (callback, condition) => {
-  const mounted = React.useRef(false);
-  React.useEffect(() => {
-    if (mounted.current) callback();
-    else mounted.current = true;
-  }, condition);
+    const userDidUpdate = useCallback(() => {
+        if (!condition || !condition()) return;
+        callback();
+    }, [callback, condition]);
+
+    useEffect(() => {
+        userDidUpdate();
+    }, [userDidUpdate]);
 };
+
+const useComponentWillUpdate = (callback, condition) => {
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,7 +1,12 @@

 const useComponentDidUpdate = (callback, condition) => {
-  const mounted = React.useRef(false);
-  React.useEffect(() => {
-    if (mounted.current) callback();
-    else mounted.current = true;
-  }, condition);
-};
+  const didUpdate = useCallback(
+    (previousProps, previousState) => {
+      if (condition) {
+        callback(previousProps, previousState);
+      }
+    },
+    [callback, condition]
+  );
+  useEffect(() => {
+    return didUpdate;
+  }, [didUpdate]);
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,7 +1,9 @@

 const useComponentDidUpdate = (callback, condition) => {
-  const mounted = React.useRef(false);
-  React.useEffect(() => {
-    if (mounted.current) callback();
-    else mounted.current = true;
-  }, condition);
+  useEffect(() => {
+    if (condition) {
+      callback();
+    }
+  });
 };
+
+export default useComponentDidUpdate;
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,7 +1,12 @@

 const useComponentDidUpdate = (callback, condition) => {
-  const mounted = React.useRef(false);
-  React.useEffect(() => {
-    if (mounted.current) callback();
-    else mounted.current = true;
-  }, condition);
-};
+  const prevProps = useRef();
+  const prevState = useRef();
+
+  useEffect(() => {
+    if (condition) {
+      callback();
+    }
+  }, [callback, condition]);
+
+  useEffect(() => {
+    prevProps.current = props;
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,7 +1,12 @@

 const useComponentDidUpdate = (callback, condition) => {
-  const mounted = React.useRef(false);
-  React.useEffect(() => {
-    if (mounted.current) callback();
-    else mounted.current = true;
-  }, condition);
-};
+  const prevProps = useRef();
+  const prevState = useRef();
+
+  const safeCallback = useCallback(callback, [callback]);
+
+  useEffect(() => {
+    if (condition(prevProps.current, prevState.current)) {
+      safeCallback();
+    }
+  }, [condition, safeCallback]);
+
```

### Toggle (task/55)

#### canonical solution

```javascript
const Toggle = ({ defaultToggled = false }) => {
  const [isToggleOn, setIsToggleOn] = React.useState(defaultToggled);

  return (
    <label className={isToggleOn ? 'toggle on' : 'toggle off'}>
      <input
        type="checkbox"
        checked={isToggleOn}
        onChange={() => setIsToggleOn(!isToggleOn)}
      />
      {isToggleOn ? 'ON' : 'OFF'}
    </label>
  );
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,14 +1,15 @@

 const Toggle = ({ defaultToggled = false }) => {
-  const [isToggleOn, setIsToggleOn] = React.useState(defaultToggled);
+  const [toggled, setToggled] = useState(defaultToggled);
+
+  const handleClick = () => {
+    setToggled(!toggled);
+  };
 
   return (
-    <label className={isToggleOn ? 'toggle on' : 'toggle off'}>
-      <input
-        type="checkbox"
-        checked={isToggleOn}
-        onChange={() => setIsToggleOn(!isToggleOn)}
-      />
-      {isToggleOn ? 'ON' : 'OFF'}
-    </label>
+    <button onClick={handleClick}>
+      {toggled ? "Toggled" : "Untoggled"}
+    </button>
   );
 };
+
+export default Toggle;
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,14 +1,9 @@

 const Toggle = ({ defaultToggled = false }) => {
-  const [isToggleOn, setIsToggleOn] = React.useState(defaultToggled);
+  const [isToggled, setIsToggled] = useState(defaultToggled);
+
+  const toggle = () => setIsToggled(!isToggled);
 
   return (
-    <label className={isToggleOn ? 'toggle on' : 'toggle off'}>
-      <input
-        type="checkbox"
-        checked={isToggleOn}
-        onChange={() => setIsToggleOn(!isToggleOn)}
-      />
-      {isToggleOn ? 'ON' : 'OFF'}
-    </label>
-  );
-};
+    <button className="toggle" onClick={toggle}>
+      <span className="toggle__round" />
+      <span className="toggle__label">{isToggled ? 'ON' : 'OFF'}
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,14 +1,15 @@

 const Toggle = ({ defaultToggled = false }) => {
-  const [isToggleOn, setIsToggleOn] = React.useState(defaultToggled);
+  const [toggled, setToggled] = useState(defaultToggled);
+
+  const toggle = () => setToggled(!toggled);
 
   return (
-    <label className={isToggleOn ? 'toggle on' : 'toggle off'}>
-      <input
-        type="checkbox"
-        checked={isToggleOn}
-        onChange={() => setIsToggleOn(!isToggleOn)}
-      />
-      {isToggleOn ? 'ON' : 'OFF'}
-    </label>
-  );
-};
+    <div>
+      <label htmlFor="toggle">
+        <input
+          id="toggle"
+          type="checkbox"
+          checked={toggled}
+          onChange={toggle}
+        />
+        {toggled ?
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,14 +1,12 @@

 const Toggle = ({ defaultToggled = false }) => {
-  const [isToggleOn, setIsToggleOn] = React.useState(defaultToggled);
+  const [isToggled, setIsToggled] = useState(defaultToggled);
+
+  const handleToggle = () => {
+    setIsToggled(!isToggled);
+  };
 
   return (
-    <label className={isToggleOn ? 'toggle on' : 'toggle off'}>
-      <input
-        type="checkbox"
-        checked={isToggleOn}
-        onChange={() => setIsToggleOn(!isToggleOn)}
-      />
-      {isToggleOn ? 'ON' : 'OFF'}
-    </label>
-  );
-};
+    <Container isToggled={isToggled}>
+      <SwitchLabel>
+        <SwitchToggle onClick={handleToggle}>
+          <SwitchToggleText isT
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,14 +1,13 @@

 const Toggle = ({ defaultToggled = false }) => {
-  const [isToggleOn, setIsToggleOn] = React.useState(defaultToggled);
+  const [toggled, setToggled] = useState(defaultToggled);
+
+  const toggle = () => setToggled(!toggled);
 
   return (
-    <label className={isToggleOn ? 'toggle on' : 'toggle off'}>
-      <input
-        type="checkbox"
-        checked={isToggleOn}
-        onChange={() => setIsToggleOn(!isToggleOn)}
-      />
-      {isToggleOn ? 'ON' : 'OFF'}
-    </label>
+    <ToggleButton onClick={toggle} toggled={toggled}>
+      {toggled ? "Yes" : "No"}
+    </ToggleButton>
   );
 };
+
+export default Toggle;
```

### MappedTable (task/56)

#### canonical solution

```javascript
const MappedTable = ({ data, propertyNames }) => {
  let filteredData = data.map(v =>
    Object.keys(v)
      .filter(k => propertyNames.includes(k))
      .reduce((acc, key) => ((acc[key] = v[key]), acc), {})
  );
  return (
    <table>
      <thead>
        <tr>
          {propertyNames.map(val => (
            <th key={`h_${val}`}>{val}</th>
          ))}
        </tr>
      </thead>
      <tbody>
        {filteredData.map((val, i) => (
          <tr key={`i_${i}`}>
            {propertyNames.map(p => (
              <td key={`i_${i}_${p}`}>{val[p]}</td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,27 +1,13 @@

 const MappedTable = ({ data, propertyNames }) => {
-  let filteredData = data.map(v =>
-    Object.keys(v)
-      .filter(k => propertyNames.includes(k))
-      .reduce((acc, key) => ((acc[key] = v[key]), acc), {})
-  );
-  return (
-    <table>
-      <thead>
-        <tr>
-          {propertyNames.map(val => (
-            <th key={`h_${val}`}>{val}</th>
-          ))}
-        </tr>
-      </thead>
-      <tbody>
-        {filteredData.map((val, i) => (
-          <tr key={`i_${i}`}>
-            {propertyNames.map(p => (
-              <td key={`i_${i}_${p}`}>{val[p]}</td>
-            ))}
-          </tr>
-        ))}
-      </tbody>
-    </table>
-  );
-};
+  const colums = propertyNames.map(propertyName => {
+    const func = (value, row) => {
+      if (value) {
+        const [key, value] = value.split(':');
+        const property = getProperty(row, key);
+        return property ? property[value] : null;
+      }
+      return null;
+    };
+    return {
+      title: propertyName,
+      dataIndex
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,27 +1,14 @@

 const MappedTable = ({ data, propertyNames }) => {
-  let filteredData = data.map(v =>
-    Object.keys(v)
-      .filter(k => propertyNames.includes(k))
-      .reduce((acc, key) => ((acc[key] = v[key]), acc), {})
-  );
-  return (
-    <table>
-      <thead>
-        <tr>
-          {propertyNames.map(val => (
-            <th key={`h_${val}`}>{val}</th>
-          ))}
-        </tr>
-      </thead>
-      <tbody>
-        {filteredData.map((val, i) => (
-          <tr key={`i_${i}`}>
-            {propertyNames.map(p => (
-              <td key={`i_${i}_${p}`}>{val[p]}</td>
-            ))}
-          </tr>
-        ))}
-      </tbody>
-    </table>
-  );
+  const mapped = data.map(entry => {
+    const mappedRow = propertyNames.map(prop => entry[prop]);
+    return mappedRow;
+  });
+  return mapped;
 };
+
+MappedTable.propTypes = {
+  data: PropTypes.arrayOf(PropTypes.object).isRequired,
+  propertyNames: PropTypes.arrayOf(PropTypes.string).isRequired,
+};
+
+export default M
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,27 +1,12 @@

 const MappedTable = ({ data, propertyNames }) => {
-  let filteredData = data.map(v =>
-    Object.keys(v)
-      .filter(k => propertyNames.includes(k))
-      .reduce((acc, key) => ((acc[key] = v[key]), acc), {})
-  );
+  const mappedData = _.map(data, ({ id, ...row }) => ({
+    id,
+    ..._.mapValues(row, value => (_.isArray(value) ? value.join(', ') : value))
+  }));
+
   return (
-    <table>
-      <thead>
-        <tr>
-          {propertyNames.map(val => (
-            <th key={`h_${val}`}>{val}</th>
-          ))}
-        </tr>
-      </thead>
-      <tbody>
-        {filteredData.map((val, i) => (
-          <tr key={`i_${i}`}>
-            {propertyNames.map(p => (
-              <td key={`i_${i}_${p}`}>{val[p]}</td>
-            ))}
-          </tr>
-        ))}
-      </tbody>
-    </table>
-  );
-};
+    <Table
+      headers={propertyNames}
+      data={mappedData}
+      className="table-sm"
+      onRowClick={() => null}
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,27 +1,14 @@

 const MappedTable = ({ data, propertyNames }) => {
-  let filteredData = data.map(v =>
-    Object.keys(v)
-      .filter(k => propertyNames.includes(k))
-      .reduce((acc, key) => ((acc[key] = v[key]), acc), {})
-  );
   return (
-    <table>
+    <table className="table table-striped">
       <thead>
         <tr>
-          {propertyNames.map(val => (
-            <th key={`h_${val}`}>{val}</th>
-          ))}
+          {propertyNames.map(propertyName => {
+            return <th key={propertyName}>{propertyName}</th>;
+          })}
         </tr>
       </thead>
       <tbody>
-        {filteredData.map((val, i) => (
-          <tr key={`i_${i}`}>
-            {propertyNames.map(p => (
-              <td key={`i_${i}_${p}`}>{val[p]}</td>
-            ))}
-          </tr>
-        ))}
-      </tbody>
-    </table>
-  );
-};
+        {data.map(value => {
+          return (
+            <tr key
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,27 +1,11 @@

 const MappedTable = ({ data, propertyNames }) => {
-  let filteredData = data.map(v =>
-    Object.keys(v)
-      .filter(k => propertyNames.includes(k))
-      .reduce((acc, key) => ((acc[key] = v[key]), acc), {})
-  );
   return (
-    <table>
-      <thead>
-        <tr>
-          {propertyNames.map(val => (
-            <th key={`h_${val}`}>{val}</th>
-          ))}
-        </tr>
-      </thead>
-      <tbody>
-        {filteredData.map((val, i) => (
-          <tr key={`i_${i}`}>
-            {propertyNames.map(p => (
-              <td key={`i_${i}_${p}`}>{val[p]}</td>
-            ))}
-          </tr>
-        ))}
-      </tbody>
-    </table>
+    <>
+      {propertyNames.map((name, index) => (
+        <td key={name}>{data[index]}</td>
+      ))}
+    </>
   );
 };
+
+export default MappedTable;
```

### useEventListener (task/57)

#### canonical solution

```javascript
const useEventListener = (type, handler, el = window) => {
  const savedHandler = React.useRef();

  React.useEffect(() => {
    savedHandler.current = handler;
  }, [handler]);

  React.useEffect(() => {
    const listener = e => savedHandler.current(e);

    el.addEventListener(type, listener);

    return () => {
      el.removeEventListener(type, listener);
    };
  }, [type, el]);
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,17 +1,9 @@

 const useEventListener = (type, handler, el = window) => {
-  const savedHandler = React.useRef();
+  el.addEventListener(type, handler)
 
-  React.useEffect(() => {
-    savedHandler.current = handler;
-  }, [handler]);
+  return () => {
+    el.removeEventListener(type, handler)
+  }
+}
 
-  React.useEffect(() => {
-    const listener = e => savedHandler.current(e);
-
-    el.addEventListener(type, listener);
-
-    return () => {
-      el.removeEventListener(type, listener);
-    };
-  }, [type, el]);
-};
+export default useEventListener
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,17 +1,13 @@

 const useEventListener = (type, handler, el = window) => {
-  const savedHandler = React.useRef();
+  el.addEventListener(type, handler);
+  return () => el.removeEventListener(type, handler);
+};
 
-  React.useEffect(() => {
-    savedHandler.current = handler;
-  }, [handler]);
+export const useLockBodyScroll = () => {
+  const [, toggle] = useLockBodyScrollState();
+  return toggle;
+};
 
-  React.useEffect(() => {
-    const listener = e => savedHandler.current(e);
-
-    el.addEventListener(type, listener);
-
-    return () => {
-      el.removeEventListener(type, listener);
-    };
-  }, [type, el]);
-};
+export const useLockBodyScrollState = () => {
+  const [locked, setLocked] = useState(false);
+  const toggle = () => set
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,17 +1,11 @@

 const useEventListener = (type, handler, el = window) => {
-  const savedHandler = React.useRef();
+    el.addEventListener(type, handler);
+    return () => el.removeEventListener(type, handler);
+};
 
-  React.useEffect(() => {
-    savedHandler.current = handler;
-  }, [handler]);
+const useEventCallback = (type, callback) => {
+    const handler = useCallback(event => callback(event), []);
+    useEventListener(type, handler);
+};
 
-  React.useEffect(() => {
-    const listener = e => savedHandler.current(e);
-
-    el.addEventListener(type, listener);
-
-    return () => {
-      el.removeEventListener(type, listener);
-    };
-  }, [type, el]);
-};
+export { useEventListener, useEventCallback };
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,17 +1,14 @@

 const useEventListener = (type, handler, el = window) => {
-  const savedHandler = React.useRef();
+    el.addEventListener(type, handler);
+    return () => el.removeEventListener(type, handler);
+};
 
-  React.useEffect(() => {
-    savedHandler.current = handler;
-  }, [handler]);
+const useWindowSize = () => {
+    const [windowSize, setWindowSize] = useState(() => ({
+        width: window.innerWidth,
+        height: window.innerHeight,
+    }));
 
-  React.useEffect(() => {
-    const listener = e => savedHandler.current(e);
-
-    el.addEventListener(type, listener);
-
-    return () => {
-      el.removeEventListener(type, listener);
-    };
-  }, [type, el]);
-};
+    useEffect(() => {
+        const handleResize = () => {
+           
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,17 +1,10 @@

 const useEventListener = (type, handler, el = window) => {
-  const savedHandler = React.useRef();
+  el.addEventListener(type, handler);
+  return () => el.removeEventListener(type, handler);
+};
 
-  React.useEffect(() => {
-    savedHandler.current = handler;
-  }, [handler]);
-
-  React.useEffect(() => {
-    const listener = e => savedHandler.current(e);
-
-    el.addEventListener(type, listener);
-
-    return () => {
-      el.removeEventListener(type, listener);
-    };
-  }, [type, el]);
-};
+function App() {
+  const [userList, setUserList] = useState([]);
+  const [userName, setUserName] = useState("");
+  const [msgList, setMsgList] = useState([]);
+  const [user, setUser] = useState({});
```

### Callto (task/58)

#### canonical solution

```javascript
const Callto = ({ phone, children }) => {
  return <a href={`tel:${phone}`}>{children}</a>;
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,3 +1,8 @@

 const Callto = ({ phone, children }) => {
-  return <a href={`tel:${phone}`}>{children}</a>;
-};
+  return (
+    <a href={`tel:${phone}`}>
+      <div className="callto">
+        <span className="callto__icon">
+          <Icon name="phone" />
+        </span>
+        <span className="callto__text">{children}</span>
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,3 +1,8 @@

 const Callto = ({ phone, children }) => {
-  return <a href={`tel:${phone}`}>{children}</a>;
+  return (
+    <CalltoButton href={`tel:${phone}`} target="_blank">
+      {children}
+    </CalltoButton>
+  );
 };
+
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,3 +1,8 @@

 const Callto = ({ phone, children }) => {
-  return <a href={`tel:${phone}`}>{children}</a>;
+  return (
+    <a href={`tel:${phone}`} className="text-yellow-500 hover:text-yellow-800">
+      {children}
+    </a>
+  );
 };
+
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,3 +1,8 @@

 const Callto = ({ phone, children }) => {
-  return <a href={`tel:${phone}`}>{children}</a>;
-};
+  return (
+    <>
+      <a
+        className="callto"
+        href={`tel:${phone}`}
+        target="_blank"
+        rel="noopener noreferrer"
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,3 +1,8 @@

 const Callto = ({ phone, children }) => {
-  return <a href={`tel:${phone}`}>{children}</a>;
+  return (
+    <div className="callto">
+      <a href={`tel:${phone}`}>{children}</a>
+    </div>
+  );
 };
+
```

### useOnWindowResize (task/59)

#### canonical solution

```javascript
const useOnWindowResize = callback => {
  const listener = React.useRef(null);

  React.useEffect(() => {
    if (listener.current)
      window.removeEventListener('resize', listener.current);
    listener.current = window.addEventListener('resize', callback);
    return () => {
      window.removeEventListener('resize', listener.current);
    };
  }, [callback]);
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,12 +1,16 @@

 const useOnWindowResize = callback => {
-  const listener = React.useRef(null);
+	const throttledCallback = useCallback(
+		throttle(callback, 200),
+		[callback]
+	);
 
-  React.useEffect(() => {
-    if (listener.current)
-      window.removeEventListener('resize', listener.current);
-    listener.current = window.addEventListener('resize', callback);
-    return () => {
-      window.removeEventListener('resize', listener.current);
-    };
-  }, [callback]);
+	useEffect(() => {
+		window.addEventListener('resize', throttledCallback);
+
+		return () => {
+			window.removeEventListener('resize', throttledCallback);
+		};
+	}, [throttledCallback]);
 };
+
+const Feed = () =>
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,12 +1,14 @@

 const useOnWindowResize = callback => {
-  const listener = React.useRef(null);
+	const onResize = useCallback(() => {
+		callback(window.innerWidth);
+	}, [callback]);
 
-  React.useEffect(() => {
-    if (listener.current)
-      window.removeEventListener('resize', listener.current);
-    listener.current = window.addEventListener('resize', callback);
-    return () => {
-      window.removeEventListener('resize', listener.current);
-    };
-  }, [callback]);
+	useEffect(() => {
+		window.addEventListener('resize', onResize);
+		return () => {
+			window.removeEventListener('resize', onResize);
+		};
+	}, [onResize]);
 };
+
+export default useOnWindowRes
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,12 +1,17 @@

 const useOnWindowResize = callback => {
-  const listener = React.useRef(null);
-
-  React.useEffect(() => {
-    if (listener.current)
-      window.removeEventListener('resize', listener.current);
-    listener.current = window.addEventListener('resize', callback);
+  useEffect(() => {
+    const listener = () => {
+      callback();
+    };
+    window.addEventListener('resize', listener);
     return () => {
-      window.removeEventListener('resize', listener.current);
+      window.removeEventListener('resize', listener);
     };
   }, [callback]);
 };
+
+const WindowListener = ({ callback }) => {
+  useOnWindowResize(callback);
+  return null;
+};
+
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,12 +1,14 @@

 const useOnWindowResize = callback => {
-  const listener = React.useRef(null);
+  const handleResize = () => {
+    callback();
+  };
 
-  React.useEffect(() => {
-    if (listener.current)
-      window.removeEventListener('resize', listener.current);
-    listener.current = window.addEventListener('resize', callback);
+  useEffect(() => {
+    window.addEventListener('resize', handleResize);
     return () => {
-      window.removeEventListener('resize', listener.current);
+      window.removeEventListener('resize', handleResize);
     };
-  }, [callback]);
+  }, []);
 };
+
+export default useOnWindowResize;
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,12 +1,15 @@

 const useOnWindowResize = callback => {
-  const listener = React.useRef(null);
+  const handleResize = () => {
+    callback();
+  };
 
-  React.useEffect(() => {
-    if (listener.current)
-      window.removeEventListener('resize', listener.current);
-    listener.current = window.addEventListener('resize', callback);
+  useEffect(() => {
+    window.addEventListener('resize', handleResize);
     return () => {
-      window.removeEventListener('resize', listener.current);
+      window.removeEventListener('resize', handleResize);
     };
-  }, [callback]);
+  }, []);
 };
+
+const useIsMobile = useCallback(() => {
+  const isMobile = useMediaQuery(MOBILE_BRE
```

### UncontrolledInput (task/60)

#### canonical solution

```javascript
const UncontrolledInput = ({ defaultValue, onValueChange, ...rest }) => {
  return (
    <input
      defaultValue={defaultValue}
      onChange={({ target: { value } }) => onValueChange(value)}
      {...rest}
    />
  );
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,9 +1,14 @@

 const UncontrolledInput = ({ defaultValue, onValueChange, ...rest }) => {
+  const [value, setValue] = useState(defaultValue);
+
+  useEffect(() => {
+    setValue(defaultValue);
+  }, [defaultValue]);
+
+  const handleValueChange = useCallback(event => {
+    setValue(event.target.value);
+    onValueChange(event.target.value);
+  }, [onValueChange]);
+
   return (
-    <input
-      defaultValue={defaultValue}
-      onChange={({ target: { value } }) => onValueChange(value)}
-      {...rest}
-    />
-  );
-};
+    <Input
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,9 +1,14 @@

 const UncontrolledInput = ({ defaultValue, onValueChange, ...rest }) => {
-  return (
-    <input
-      defaultValue={defaultValue}
-      onChange={({ target: { value } }) => onValueChange(value)}
-      {...rest}
-    />
+  const [value, setValue] = useState(defaultValue);
+
+  useEffect(() => {
+    setValue(defaultValue);
+  }, [defaultValue]);
+
+  const onChange = useCallback(
+    e => {
+      setValue(e.target.value);
+      onValueChange(e.target.value);
+    },
+    [onValueChange]
   );
-};
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,9 +1,7 @@

 const UncontrolledInput = ({ defaultValue, onValueChange, ...rest }) => {
-  return (
-    <input
-      defaultValue={defaultValue}
-      onChange={({ target: { value } }) => onValueChange(value)}
-      {...rest}
-    />
-  );
+  const onChange = useEventCallback(event => onValueChange(event.target.value));
+
+  return <input defaultValue={defaultValue} onChange={onChange} {...rest} />;
 };
+
+export default UncontrolledInput;
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,9 +1,14 @@

 const UncontrolledInput = ({ defaultValue, onValueChange, ...rest }) => {
-  return (
-    <input
-      defaultValue={defaultValue}
-      onChange={({ target: { value } }) => onValueChange(value)}
-      {...rest}
-    />
+  const [value, setValue] = useState(defaultValue);
+
+  const onChange = useCallback(
+    e => {
+      const nextValue = e.target.value;
+      setValue(nextValue);
+      onValueChange(nextValue);
+    },
+    [onValueChange]
   );
+
+  return <input onChange={onChange} {...rest} value={value} />;
 };
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,9 +1,14 @@

 const UncontrolledInput = ({ defaultValue, onValueChange, ...rest }) => {
-  return (
-    <input
-      defaultValue={defaultValue}
-      onChange={({ target: { value } }) => onValueChange(value)}
-      {...rest}
-    />
+  const [value, setValue] = useState(defaultValue);
+
+  useEffect(() => {
+    setValue(defaultValue);
+  }, [defaultValue]);
+
+  const handleValueChange = useCallback(
+    e => {
+      setValue(e.target.value);
+      onValueChange(e.target.value);
+    },
+    [onValueChange]
   );
-};
```

### TextArea (task/61)

#### canonical solution

```javascript
const TextArea = ({
  cols = 20,
  rows = 2,
  defaultValue,
  onValueChange,
  ...rest
}) => {
  return (
    <textarea
      cols={cols}
      rows={rows}
      defaultValue={defaultValue}
      onChange={({ target: { value } }) => onValueChange(value)}
      {...rest}
    />
  );
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,16 +1,9 @@

-const TextArea = ({  cols = 20,
-  rows = 2,
-  defaultValue,
-  onValueChange,
-  ...rest
-}) => {
+const TextArea = ({ name, label, error, ...rest }) => {
   return (
-    <textarea
-      cols={cols}
-      rows={rows}
-      defaultValue={defaultValue}
-      onChange={({ target: { value } }) => onValueChange(value)}
-      {...rest}
-    />
+    <div className="form-group">
+      <label htmlFor={name}>{label}</label>
+      <textarea {...rest} name={name} id={name} className="form-control" />
+      {error && <div className="alert alert-danger">{error}</div>}
+    </div>
   );
 };
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,16 +1,11 @@

-const TextArea = ({  cols = 20,
-  rows = 2,
-  defaultValue,
-  onValueChange,
-  ...rest
-}) => {
+const TextArea = ({ label, name, value, error, onChange, onBlur, disabled, maxLength }) => {
   return (
-    <textarea
-      cols={cols}
-      rows={rows}
-      defaultValue={defaultValue}
-      onChange={({ target: { value } }) => onValueChange(value)}
-      {...rest}
-    />
-  );
-};
+    <div className="form-group">
+      <label htmlFor={name}>{label}</label>
+      <textarea
+        className="form-control"
+        id={name}
+        name={name}
+        value={value}
+        onChange={onChange}
+        onBlur={on
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,17 +1,13 @@

 const TextArea = ({
-  cols = 20,
-  rows = 2,
-  defaultValue,
-  onValueChange,
+  name,
+  placeholder,
+  value,
+  isMulti,
   ...rest
-}) => {
+}: TextAreaProps) => {
   return (
-    <textarea
-      cols={cols}
-      rows={rows}
-      defaultValue={defaultValue}
-      onChange={({ target: { value } }) => onValueChange(value)}
-      {...rest}
-    />
+    <StyledTextArea name={name} placeholder={placeholder} value={value} {...rest} />
   );
 };
+
+export default TextArea;
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,17 +1,16 @@

 const TextArea = ({
-  cols = 20,
-  rows = 2,
-  defaultValue,
-  onValueChange,
+  name,
+  label,
+  error,
   ...rest
 }) => {
   return (
-    <textarea
-      cols={cols}
-      rows={rows}
-      defaultValue={defaultValue}
-      onChange={({ target: { value } }) => onValueChange(value)}
-      {...rest}
-    />
-  );
-};
+    <div className="form-group">
+      <label htmlFor={name}>{label}</label>
+      <textarea
+        className="form-control"
+        id={name}
+        name={name}
+        {...rest}
+      />
+      {error && <div className="alert alert-danger
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,16 +1,12 @@

-const TextArea = ({  cols = 20,
-  rows = 2,
-  defaultValue,
-  onValueChange,
-  ...rest
-}) => {
+const TextArea = ({ name, rows, label, error, ...rest }) => {
   return (
-    <textarea
-      cols={cols}
-      rows={rows}
-      defaultValue={defaultValue}
-      onChange={({ target: { value } }) => onValueChange(value)}
-      {...rest}
-    />
-  );
-};
+    <div className="form-group">
+      <label htmlFor={name}>{label}</label>
+      <textarea
+        className="form-control"
+        rows={rows}
+        name={name}
+        id={name}
+        {...rest}
+      />
+      {error && <div className="alert alert-danger">
```

### useScript (task/62)

#### canonical solution

```javascript
const useScript = src => {
  const [status, setStatus] = React.useState(src ? 'loading' : 'idle');

  React.useEffect(() => {
    if (!src) {
      setStatus('idle');
      return;
    }

    let script = document.querySelector(`script[src="${src}"]`);

    if (!script) {
      script = document.createElement('script');
      script.src = src;
      script.async = true;
      script.setAttribute('data-status', 'loading');
      document.body.appendChild(script);

      const setDataStatus = event => {
        script.setAttribute(
          'data-status',
          event.type === 'load' ? 'ready' : 'error'
        );
      };
      script.addEventListener('load', setDataStatus);
      script.addEventListener('error', setDataStatus);
    } else {
      setStatus(script.getAttribute('data-status'));
    }

    const setStateStatus = event => {
      setStatus(event.type === 'load' ? 'ready' : 'error');
    };

    script.addEventListener('load', setStateStatus);
    script.addEventListener('error', setStateStatus);

    return () => {
      if (script) {
        script.removeEventListener('load', setStateStatus);
        script.removeEventListener('error', setStateStatus);
      }
    };
  }, [src]);

  return status;
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,47 +1,19 @@

 const useScript = src => {
-  const [status, setStatus] = React.useState(src ? 'loading' : 'idle');
+    const [state, setState] = useState({
+        loaded: false,
+        error: false
+    });
 
-  React.useEffect(() => {
-    if (!src) {
-      setStatus('idle');
-      return;
-    }
+    useEffect(() => {
+        const script = document.createElement("script");
+        script.src = src;
+        script.async = true;
 
-    let script = document.querySelector(`script[src="${src}"]`);
+        script.onload = () => {
+            setState({
+                loaded: true,
+                error: false
+            });
+        };
 
-    if (!script) {
-      script = document.createElement('script');
-      script.src = src;
-      script.async = true;
-      script.setAttribute('data-status', 'loading');
-      document.body.appendChild(script);
-
-      const setDataStatus = event => {
-        script.setAttribute(
-          'data-status',
-          event.type === 'load' ? 'ready' : 'error'
-        );
-      };
-      script.addEventListener('load', setDataStatus);
-      script.addEventListener('error', setDataStatus);
-    } else {
-      setStatus(script.getAttribute('data-status'));
-    }
-
-    const setStateStatus = event => {
-      setStatus(event.type === 'load' ? 'ready' : 'error');
-    };
-
-    script.addEventListener('load', setStateStatus);
-    script.addEventListener('error', setStateStatus);
-
-    return () => {
-      if (script) {
-        script.removeEventListener('load', setStateStatus);
-        script.removeEventListener('error', setStateStatus);
-      }
-    };
-  }, [src]);
-
-  return status;
-};
+        script
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,47 +1,19 @@

 const useScript = src => {
-  const [status, setStatus] = React.useState(src ? 'loading' : 'idle');
+    const [state, setState] = useState({
+        loaded: false,
+        error: false
+    });
 
-  React.useEffect(() => {
-    if (!src) {
-      setStatus('idle');
-      return;
-    }
+    useEffect(() => {
+        const script = document.createElement('script');
+        script.src = src;
+        script.async = true;
 
-    let script = document.querySelector(`script[src="${src}"]`);
+        script.onload = () => {
+            setState({
+                loaded: true,
+                error: false
+            });
+        };
 
-    if (!script) {
-      script = document.createElement('script');
-      script.src = src;
-      script.async = true;
-      script.setAttribute('data-status', 'loading');
-      document.body.appendChild(script);
-
-      const setDataStatus = event => {
-        script.setAttribute(
-          'data-status',
-          event.type === 'load' ? 'ready' : 'error'
-        );
-      };
-      script.addEventListener('load', setDataStatus);
-      script.addEventListener('error', setDataStatus);
-    } else {
-      setStatus(script.getAttribute('data-status'));
-    }
-
-    const setStateStatus = event => {
-      setStatus(event.type === 'load' ? 'ready' : 'error');
-    };
-
-    script.addEventListener('load', setStateStatus);
-    script.addEventListener('error', setStateStatus);
-
-    return () => {
-      if (script) {
-        script.removeEventListener('load', setStateStatus);
-        script.removeEventListener('error', setStateStatus);
-      }
-    };
-  }, [src]);
-
-  return status;
-};
+        script
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,47 +1,13 @@

 const useScript = src => {
-  const [status, setStatus] = React.useState(src ? 'loading' : 'idle');
+  let script = document.createElement('script');
+  script.src = src;
+  script.async = true;
+  document.body.appendChild(script);
+};
 
-  React.useEffect(() => {
-    if (!src) {
-      setStatus('idle');
-      return;
-    }
-
-    let script = document.querySelector(`script[src="${src}"]`);
-
-    if (!script) {
-      script = document.createElement('script');
-      script.src = src;
-      script.async = true;
-      script.setAttribute('data-status', 'loading');
-      document.body.appendChild(script);
-
-      const setDataStatus = event => {
-        script.setAttribute(
-          'data-status',
-          event.type === 'load' ? 'ready' : 'error'
-        );
-      };
-      script.addEventListener('load', setDataStatus);
-      script.addEventListener('error', setDataStatus);
-    } else {
-      setStatus(script.getAttribute('data-status'));
-    }
-
-    const setStateStatus = event => {
-      setStatus(event.type === 'load' ? 'ready' : 'error');
-    };
-
-    script.addEventListener('load', setStateStatus);
-    script.addEventListener('error', setStateStatus);
-
-    return () => {
-      if (script) {
-        script.removeEventListener('load', setStateStatus);
-        script.removeEventListener('error', setStateStatus);
-      }
-    };
-  }, [src]);
-
-  return status;
-};
+// IFrame
+const IFrame = ({ src, height, width, ...rest }) => {
+  const props = { ...rest };
+  const iframe = useRef(null);
+  const scriptSrc =
+    src.indexOf('http
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,47 +1,13 @@

 const useScript = src => {
-  const [status, setStatus] = React.useState(src ? 'loading' : 'idle');
+    useEffect(() => {
+        const script = document.createElement('script');
+        script.src = src;
+        document.body.appendChild(script);
+        return () => {
+            document.body.removeChild(script);
+        };
+    }, [src]);
+};
 
-  React.useEffect(() => {
-    if (!src) {
-      setStatus('idle');
-      return;
-    }
-
-    let script = document.querySelector(`script[src="${src}"]`);
-
-    if (!script) {
-      script = document.createElement('script');
-      script.src = src;
-      script.async = true;
-      script.setAttribute('data-status', 'loading');
-      document.body.appendChild(script);
-
-      const setDataStatus = event => {
-        script.setAttribute(
-          'data-status',
-          event.type === 'load' ? 'ready' : 'error'
-        );
-      };
-      script.addEventListener('load', setDataStatus);
-      script.addEventListener('error', setDataStatus);
-    } else {
-      setStatus(script.getAttribute('data-status'));
-    }
-
-    const setStateStatus = event => {
-      setStatus(event.type === 'load' ? 'ready' : 'error');
-    };
-
-    script.addEventListener('load', setStateStatus);
-    script.addEventListener('error', setStateStatus);
-
-    return () => {
-      if (script) {
-        script.removeEventListener('load', setStateStatus);
-        script.removeEventListener('error', setStateStatus);
-      }
-    };
-  }, [src]);
-
-  return status;
-};
+export default function Sankey({ height, width, data }) {
+    useScript('https://unpkg.com/@antv/data
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,47 +1,15 @@

 const useScript = src => {
-  const [status, setStatus] = React.useState(src ? 'loading' : 'idle');
+  const ref = useRef()
+  useEffect(() => {
+    if (!ref.current) {
+      const script = document.createElement('script')
+      script.src = src
+      ref.current = script
+      document.body.appendChild(script)
+    }
+  }, [src]) // Only re-run if value changes
+  return ref
+}
 
-  React.useEffect(() => {
-    if (!src) {
-      setStatus('idle');
-      return;
-    }
-
-    let script = document.querySelector(`script[src="${src}"]`);
-
-    if (!script) {
-      script = document.createElement('script');
-      script.src = src;
-      script.async = true;
-      script.setAttribute('data-status', 'loading');
-      document.body.appendChild(script);
-
-      const setDataStatus = event => {
-        script.setAttribute(
-          'data-status',
-          event.type === 'load' ? 'ready' : 'error'
-        );
-      };
-      script.addEventListener('load', setDataStatus);
-      script.addEventListener('error', setDataStatus);
-    } else {
-      setStatus(script.getAttribute('data-status'));
-    }
-
-    const setStateStatus = event => {
-      setStatus(event.type === 'load' ? 'ready' : 'error');
-    };
-
-    script.addEventListener('load', setStateStatus);
-    script.addEventListener('error', setStateStatus);
-
-    return () => {
-      if (script) {
-        script.removeEventListener('load', setStateStatus);
-        script.removeEventListener('error', setStateStatus);
-      }
-    };
-  }, [src]);
-
-  return status;
-};
+const useStyles = makeStyles({
+  img
```

### useRequestAnimationFrame (task/63)

#### canonical solution

```javascript
const useRequestAnimationFrame = callback => {
  const requestRef = React.useRef();
  const previousTimeRef = React.useRef();

  const animate = time => {
    if (previousTimeRef.current) callback(time - previousTimeRef.current);
    previousTimeRef.current = time;
    requestRef.current = requestAnimationFrame(animate);
  };

  React.useEffect(() => {
    requestRef.current = requestAnimationFrame(animate);
    return () => cancelAnimationFrame(requestRef.current);
  }, []);
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,15 +1,11 @@

 const useRequestAnimationFrame = callback => {
-  const requestRef = React.useRef();
-  const previousTimeRef = React.useRef();
-
-  const animate = time => {
-    if (previousTimeRef.current) callback(time - previousTimeRef.current);
-    previousTimeRef.current = time;
-    requestRef.current = requestAnimationFrame(animate);
-  };
-
-  React.useEffect(() => {
-    requestRef.current = requestAnimationFrame(animate);
-    return () => cancelAnimationFrame(requestRef.current);
-  }, []);
-};
+  const requestAnimationFrame =
+    window.requestAnimationFrame ||
+    window.mozRequestAnimationFrame ||
+    window.webkitRequestAnimationFrame ||
+    window.msRequestAnimationFrame;
+  const frameDeadline = window.performance.now() + FRAME_THRESHOLD;
+  requestAnimationFrame(callback);
+  return () => {
+    requestAnimationFrame(() => {
+      if (window.performance.now() >=
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,15 +1,14 @@

 const useRequestAnimationFrame = callback => {
-  const requestRef = React.useRef();
-  const previousTimeRef = React.useRef();
+    const requestAnimationFrame =
+        window.requestAnimationFrame ||
+        window.mozRequestAnimationFrame ||
+        window.webkitRequestAnimationFrame ||
+        window.msRequestAnimationFrame;
+    const raf = requestAnimationFrame(callback);
+    return () => {
+        requestAnimationFrame.cancel(raf);
+    };
+};
 
-  const animate = time => {
-    if (previousTimeRef.current) callback(time - previousTimeRef.current);
-    previousTimeRef.current = time;
-    requestRef.current = requestAnimationFrame(animate);
-  };
-
-  React.useEffect(() => {
-    requestRef.current = requestAnimationFrame(animate);
-    return () => cancelAnimationFrame(requestRef.current);
-  }, []);
-};
+const useMouseCoords = initialX => {
+    const [mouseX, setMouseX
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,15 +1,9 @@

 const useRequestAnimationFrame = callback => {
-  const requestRef = React.useRef();
-  const previousTimeRef = React.useRef();
+  const element = useRef();
+  useEffect(() => {
+    element.current = requestAnimationFrame(callback);
+    return () => cancelAnimationFrame(element.current);
+  }, [callback]);
+};
 
-  const animate = time => {
-    if (previousTimeRef.current) callback(time - previousTimeRef.current);
-    previousTimeRef.current = time;
-    requestRef.current = requestAnimationFrame(animate);
-  };
-
-  React.useEffect(() => {
-    requestRef.current = requestAnimationFrame(animate);
-    return () => cancelAnimationFrame(requestRef.current);
-  }, []);
-};
+export default useRequestAnimationFrame;
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,15 +1,15 @@

 const useRequestAnimationFrame = callback => {
-  const requestRef = React.useRef();
-  const previousTimeRef = React.useRef();
+  const savedCallback = useRef();
 
-  const animate = time => {
-    if (previousTimeRef.current) callback(time - previousTimeRef.current);
-    previousTimeRef.current = time;
-    requestRef.current = requestAnimationFrame(animate);
-  };
+  // Remember the latest callback.
+  useEffect(() => {
+    savedCallback.current = callback;
+  }, [callback]);
 
-  React.useEffect(() => {
-    requestRef.current = requestAnimationFrame(animate);
-    return () => cancelAnimationFrame(requestRef.current);
-  }, []);
-};
+  // Set up the interval.
+  useEffect(() => {
+    function tick() {
+      savedCallback.current();
+    }
+    if (savedCallback.current) {
+      const id = setInterval(tick, 1000 / 60);
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,15 +1,16 @@

 const useRequestAnimationFrame = callback => {
-  const requestRef = React.useRef();
-  const previousTimeRef = React.useRef();
+  const frame = requestAnimationFrame(() => {
+    if (frame !== null) {
+      cancelAnimationFrame(frame);
+    }
+    callback();
+  });
+};
 
-  const animate = time => {
-    if (previousTimeRef.current) callback(time - previousTimeRef.current);
-    previousTimeRef.current = time;
-    requestRef.current = requestAnimationFrame(animate);
-  };
-
-  React.useEffect(() => {
-    requestRef.current = requestAnimationFrame(animate);
-    return () => cancelAnimationFrame(requestRef.current);
-  }, []);
-};
+const useInterval = (callback, delay) => {
+  const interval = setInterval(callback, delay);
+  useEffect(() => {
+    return () => {
+      clearInterval(interval);
+    };
+  }, [
```

### useSet (task/64)

#### canonical solution

```javascript
const useSet = initialValue => {
  const [set, setSet] = React.useState(new Set(initialValue));

  const actions = React.useMemo(
    () => ({
      add: item => setSet(prevSet => new Set([...prevSet, item])),
      remove: item =>
        setSet(prevSet => new Set([...prevSet].filter(i => i !== item))),
      clear: () => setSet(new Set()),
    }),
    [setSet]
  );

  return [set, actions];
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,15 +1,6 @@

 const useSet = initialValue => {
-  const [set, setSet] = React.useState(new Set(initialValue));
+    const [value, setValue] = useState(initialValue);
+    return [value, setValue];
+};
 
-  const actions = React.useMemo(
-    () => ({
-      add: item => setSet(prevSet => new Set([...prevSet, item])),
-      remove: item =>
-        setSet(prevSet => new Set([...prevSet].filter(i => i !== item))),
-      clear: () => setSet(new Set()),
-    }),
-    [setSet]
-  );
-
-  return [set, actions];
-};
+export default useSet;
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,15 +1,6 @@

 const useSet = initialValue => {
-  const [set, setSet] = React.useState(new Set(initialValue));
+  const [state, setState] = useState(initialValue);
+  return [state, setState];
+};
 
-  const actions = React.useMemo(
-    () => ({
-      add: item => setSet(prevSet => new Set([...prevSet, item])),
-      remove: item =>
-        setSet(prevSet => new Set([...prevSet].filter(i => i !== item))),
-      clear: () => setSet(new Set()),
-    }),
-    [setSet]
-  );
-
-  return [set, actions];
-};
+export default useSet;
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,15 +1,15 @@

 const useSet = initialValue => {
-  const [set, setSet] = React.useState(new Set(initialValue));
+  const [state, setState] = useState(initialValue);
+  return [state, setState];
+};
 
-  const actions = React.useMemo(
-    () => ({
-      add: item => setSet(prevSet => new Set([...prevSet, item])),
-      remove: item =>
-        setSet(prevSet => new Set([...prevSet].filter(i => i !== item))),
-      clear: () => setSet(new Set()),
-    }),
-    [setSet]
-  );
-
-  return [set, actions];
+const useSubscribe = (callback, deps) => {
+  const [, forceUpdate] = useState();
+  useEffect(() => {
+    callback();
+    return () => {
+      callback = () => {};
+    };
+  }, deps || []);
+  return forceUpdate;
 };
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,15 +1,6 @@

 const useSet = initialValue => {
-  const [set, setSet] = React.useState(new Set(initialValue));
+  const [value, setValue] = useState(initialValue);
+  return [value, setValue];
+};
 
-  const actions = React.useMemo(
-    () => ({
-      add: item => setSet(prevSet => new Set([...prevSet, item])),
-      remove: item =>
-        setSet(prevSet => new Set([...prevSet].filter(i => i !== item))),
-      clear: () => setSet(new Set()),
-    }),
-    [setSet]
-  );
-
-  return [set, actions];
-};
+export default useSet;
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,15 +1,6 @@

 const useSet = initialValue => {
-  const [set, setSet] = React.useState(new Set(initialValue));
+  const [value, setValue] = useState(initialValue);
+  return [value, setValue];
+};
 
-  const actions = React.useMemo(
-    () => ({
-      add: item => setSet(prevSet => new Set([...prevSet, item])),
-      remove: item =>
-        setSet(prevSet => new Set([...prevSet].filter(i => i !== item))),
-      clear: () => setSet(new Set()),
-    }),
-    [setSet]
-  );
-
-  return [set, actions];
-};
+export default useSet;
```

### useLocalStorage (task/65)

#### canonical solution

```javascript
const useLocalStorage = (keyName, defaultValue) => {
  const [storedValue, setStoredValue] = React.useState(() => {
    try {
      const value = window.localStorage.getItem(keyName);

      if (value) {
        return JSON.parse(value);
      } else {
        window.localStorage.setItem(keyName, JSON.stringify(defaultValue));
        return defaultValue;
      }
    } catch (err) {
      return defaultValue;
    }
  });

  const setValue = newValue => {
    try {
      window.localStorage.setItem(keyName, JSON.stringify(newValue));
    } catch (err) {}
    setStoredValue(newValue);
  };

  return [storedValue, setValue];
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,25 +1,14 @@

 const useLocalStorage = (keyName, defaultValue) => {
-  const [storedValue, setStoredValue] = React.useState(() => {
+  const [state, setState] = useState(() => {
     try {
-      const value = window.localStorage.getItem(keyName);
-
-      if (value) {
-        return JSON.parse(value);
-      } else {
-        window.localStorage.setItem(keyName, JSON.stringify(defaultValue));
-        return defaultValue;
-      }
-    } catch (err) {
+      const val = localStorage.getItem(keyName);
+      return val ? JSON.parse(val) : defaultValue;
+    } catch (e) {
       return defaultValue;
     }
   });
 
-  const setValue = newValue => {
-    try {
-      window.localStorage.setItem(keyName, JSON.stringify(newValue));
-    } catch (err) {}
-    setStoredValue(newValue);
-  };
-
-  return [storedValue, setValue];
-};
+  const set = useCallback(
+    val => {
+      try {
+        const valString = JSON.stringify(val);
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,25 +1,13 @@

 const useLocalStorage = (keyName, defaultValue) => {
-  const [storedValue, setStoredValue] = React.useState(() => {
+  const [storedValue, setStoredValue] = useState(() => {
     try {
-      const value = window.localStorage.getItem(keyName);
-
-      if (value) {
-        return JSON.parse(value);
-      } else {
-        window.localStorage.setItem(keyName, JSON.stringify(defaultValue));
-        return defaultValue;
-      }
-    } catch (err) {
+      const item = window.localStorage.getItem(keyName);
+      return item ? JSON.parse(item) : defaultValue;
+    } catch (error) {
+      console.log(error);
       return defaultValue;
     }
   });
 
-  const setValue = newValue => {
+  const setValue = (value) => {
     try {
-      window.localStorage.setItem(keyName, JSON.stringify(newValue));
-    } catch (err) {}
-    setStoredValue(newValue);
-  };
-
-  return [storedValue, setValue];
-};
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,25 +1,14 @@

 const useLocalStorage = (keyName, defaultValue) => {
-  const [storedValue, setStoredValue] = React.useState(() => {
-    try {
-      const value = window.localStorage.getItem(keyName);
+  const [localValue, setLocalValue] = useState(
+    getLocalStorageValue(keyName, defaultValue)
+  );
 
-      if (value) {
-        return JSON.parse(value);
-      } else {
-        window.localStorage.setItem(keyName, JSON.stringify(defaultValue));
-        return defaultValue;
-      }
-    } catch (err) {
-      return defaultValue;
-    }
-  });
-
-  const setValue = newValue => {
-    try {
-      window.localStorage.setItem(keyName, JSON.stringify(newValue));
-    } catch (err) {}
-    setStoredValue(newValue);
+  const setValue = value => {
+    setLocalValue(value);
+    setLocalStorageValue(keyName, value);
   };
 
-  return [storedValue, setValue];
+  return [localValue, setValue];
 };
+
+export default useLocalStorage;
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,25 +1,12 @@

 const useLocalStorage = (keyName, defaultValue) => {
-  const [storedValue, setStoredValue] = React.useState(() => {
-    try {
-      const value = window.localStorage.getItem(keyName);
+  const [data, setData] = useState(defaultValue);
 
-      if (value) {
-        return JSON.parse(value);
-      } else {
-        window.localStorage.setItem(keyName, JSON.stringify(defaultValue));
-        return defaultValue;
-      }
-    } catch (err) {
-      return defaultValue;
+  useEffect(() => {
+    const dataFromStorage = JSON.parse(localStorage.getItem(keyName));
+    if (dataFromStorage) {
+      setData(dataFromStorage);
     }
-  });
+  }, [keyName]);
 
-  const setValue = newValue => {
-    try {
-      window.localStorage.setItem(keyName, JSON.stringify(newValue));
-    } catch (err) {}
-    setStoredValue(newValue);
-  };
-
-  return [storedValue, setValue];
-};
+  useEffect(() => {
+    localStorage.setItem(keyName, JSON.stringify(data));
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,25 +1,13 @@

 const useLocalStorage = (keyName, defaultValue) => {
-  const [storedValue, setStoredValue] = React.useState(() => {
-    try {
-      const value = window.localStorage.getItem(keyName);
-
-      if (value) {
-        return JSON.parse(value);
-      } else {
-        window.localStorage.setItem(keyName, JSON.stringify(defaultValue));
-        return defaultValue;
-      }
-    } catch (err) {
-      return defaultValue;
+  const [data, setData] = useState(() => {
+    const storageValue = localStorage.getItem(keyName);
+    if (storageValue) {
+      return JSON.parse(storageValue);
     }
+    return defaultValue;
   });
 
-  const setValue = newValue => {
-    try {
-      window.localStorage.setItem(keyName, JSON.stringify(newValue));
-    } catch (err) {}
-    setStoredValue(newValue);
-  };
-
-  return [storedValue, setValue];
-};
+  const setLocalStorage = value => {
+    const valueToStore =
+      value instanceof Function ? value(data) : value;
+    localStorage.setItem
```

### Collapse (task/66)

#### canonical solution

```javascript
const Collapse = ({ collapsed, children }) => {
  const [isCollapsed, setIsCollapsed] = React.useState(collapsed);

  return (
    <>
      <button
        className="collapse-button"
        onClick={() => setIsCollapsed(!isCollapsed)}
      >
        {isCollapsed ? 'Show' : 'Hide'} content
      </button>
      <div
        className={`collapse-content ${isCollapsed ? 'collapsed' : 'expanded'}`}
        aria-expanded={isCollapsed}
      >
        {children}
      </div>
    </>
  );
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,20 +1,5 @@

 const Collapse = ({ collapsed, children }) => {
-  const [isCollapsed, setIsCollapsed] = React.useState(collapsed);
+  return collapsed ? null : children;
+};
 
-  return (
-    <>
-      <button
-        className="collapse-button"
-        onClick={() => setIsCollapsed(!isCollapsed)}
-      >
-        {isCollapsed ? 'Show' : 'Hide'} content
-      </button>
-      <div
-        className={`collapse-content ${isCollapsed ? 'collapsed' : 'expanded'}`}
-        aria-expanded={isCollapsed}
-      >
-        {children}
-      </div>
-    </>
-  );
-};
+export default Collapse;
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,20 +1,16 @@

 const Collapse = ({ collapsed, children }) => {
-  const [isCollapsed, setIsCollapsed] = React.useState(collapsed);
+  const [width, setWidth] = useState(getWidth(collapsed));
+
+  useEffect(() => {
+    window.addEventListener('resize', () => {
+      setWidth(getWidth(collapsed));
+    });
+  }, [collapsed]);
 
   return (
     <>
-      <button
-        className="collapse-button"
-        onClick={() => setIsCollapsed(!isCollapsed)}
-      >
-        {isCollapsed ? 'Show' : 'Hide'} content
-      </button>
       <div
-        className={`collapse-content ${isCollapsed ? 'collapsed' : 'expanded'}`}
-        aria-expanded={isCollapsed}
-      >
-        {children}
-      </div>
-    </>
-  );
-};
+        style={{
+          overflowY: 'auto',
+          overflowX: 'hidden',
+          width:
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,20 +1,12 @@

 const Collapse = ({ collapsed, children }) => {
-  const [isCollapsed, setIsCollapsed] = React.useState(collapsed);
-
-  return (
-    <>
-      <button
-        className="collapse-button"
-        onClick={() => setIsCollapsed(!isCollapsed)}
-      >
-        {isCollapsed ? 'Show' : 'Hide'} content
-      </button>
-      <div
-        className={`collapse-content ${isCollapsed ? 'collapsed' : 'expanded'}`}
-        aria-expanded={isCollapsed}
-      >
-        {children}
-      </div>
-    </>
-  );
-};
+  const isMobile = useMediaQuery({ maxWidth: 768 });
+  const containerStyle = {
+    display: 'flex',
+    flexDirection: 'column',
+    justifyContent: 'center',
+    alignItems: 'center',
+    height: isMobile ? '100vh' : 'auto',
+    margin: '0 0 1em 0',
+  };
+  const svgStyle = {
+    width: '75%
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,20 +1,16 @@

 const Collapse = ({ collapsed, children }) => {
-  const [isCollapsed, setIsCollapsed] = React.useState(collapsed);
-
+  const isOpen = !collapsed;
   return (
-    <>
-      <button
-        className="collapse-button"
-        onClick={() => setIsCollapsed(!isCollapsed)}
-      >
-        {isCollapsed ? 'Show' : 'Hide'} content
-      </button>
-      <div
-        className={`collapse-content ${isCollapsed ? 'collapsed' : 'expanded'}`}
-        aria-expanded={isCollapsed}
-      >
-        {children}
-      </div>
-    </>
+    <div className={`collapse ${isOpen ? 'is-open' : ''}`}>
+      {children}
+    </div>
   );
 };
+
+Collapse.propTypes = {
+  collapsed: PropTypes.bool,
+  children: PropTypes.node,
+};
+
+Collapse.defaultProps = {
+  collapsed: false,
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,20 +1,11 @@

 const Collapse = ({ collapsed, children }) => {
-  const [isCollapsed, setIsCollapsed] = React.useState(collapsed);
+  const style = collapsed ? { display: 'none' } : {};
+  return <div style={style}>{children}</div>;
+};
 
-  return (
-    <>
-      <button
-        className="collapse-button"
-        onClick={() => setIsCollapsed(!isCollapsed)}
-      >
-        {isCollapsed ? 'Show' : 'Hide'} content
-      </button>
-      <div
-        className={`collapse-content ${isCollapsed ? 'collapsed' : 'expanded'}`}
-        aria-expanded={isCollapsed}
-      >
-        {children}
-      </div>
-    </>
-  );
+Collapse.propTypes = {
+  collapsed: PropTypes.bool.isRequired,
+  children: PropTypes.node.isRequired,
 };
+
+export default Collapse;
```

### RippleButton (task/67)

#### canonical solution

```javascript
const RippleButton = ({ children, onClick }) => {
  const [coords, setCoords] = React.useState({ x: -1, y: -1 });
  const [isRippling, setIsRippling] = React.useState(false);

  React.useEffect(() => {
    if (coords.x !== -1 && coords.y !== -1) {
      setIsRippling(true);
      setTimeout(() => setIsRippling(false), 300);
    } else setIsRippling(false);
  }, [coords]);

  React.useEffect(() => {
    if (!isRippling) setCoords({ x: -1, y: -1 });
  }, [isRippling]);

  return (
    <button
      className="ripple-button"
      onClick={e => {
        const rect = e.target.getBoundingClientRect();
        setCoords({ x: e.clientX - rect.left, y: e.clientY - rect.top });
        onClick && onClick(e);
      }}
    >
      {isRippling ? (
        <span
          className="ripple"
          style={{
            left: coords.x,
            top: coords.y
          }}
        />
      ) : (
        ''
      )}
      <span className="content">{children}</span>
    </button>
  );
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,39 +1,16 @@

 const RippleButton = ({ children, onClick }) => {
-  const [coords, setCoords] = React.useState({ x: -1, y: -1 });
-  const [isRippling, setIsRippling] = React.useState(false);
+  const [ripples, setRipples] = useState([]);
 
-  React.useEffect(() => {
-    if (coords.x !== -1 && coords.y !== -1) {
-      setIsRippling(true);
-      setTimeout(() => setIsRippling(false), 300);
-    } else setIsRippling(false);
-  }, [coords]);
+  const startRipple = useCallback(
+    event => {
+      setRipples(prevRipples => [
+        ...prevRipples,
+        <Ripple key={Date.now()} />,
+      ]);
+    },
+    [setRipples],
+  );
 
-  React.useEffect(() => {
-    if (!isRippling) setCoords({ x: -1, y: -1 });
-  }, [isRippling]);
-
-  return (
-    <button
-      className="ripple-button"
-      onClick={e => {
-        const rect = e.target.getBoundingClientRect();
-        setCoords({ x: e.clientX - rect.left, y: e.clientY - rect.top });
-        onClick && onClick(e);
-      }}
-    >
-      {isRippling ? (
-        <span
-          className="ripple"
-          style={{
-            left: coords.x,
-            top: coords.y
-          }}
-        />
-      ) : (
-        ''
-      )}
-      <span className="content">{children}</span>
-    </button>
-  );
-};
+  const endRipple = useCallback(
+    event => {
+      set
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,39 +1,16 @@

 const RippleButton = ({ children, onClick }) => {
-  const [coords, setCoords] = React.useState({ x: -1, y: -1 });
-  const [isRippling, setIsRippling] = React.useState(false);
+  const [ripples, setRipples] = useState([]);
 
-  React.useEffect(() => {
-    if (coords.x !== -1 && coords.y !== -1) {
-      setIsRippling(true);
-      setTimeout(() => setIsRippling(false), 300);
-    } else setIsRippling(false);
-  }, [coords]);
-
-  React.useEffect(() => {
-    if (!isRippling) setCoords({ x: -1, y: -1 });
-  }, [isRippling]);
+  const clickHandler = (e) => {
+    setRipples([
+      ...ripples,
+      <Ripple key={Math.random()} />,
+    ]);
+    onClick(e);
+  };
 
   return (
-    <button
-      className="ripple-button"
-      onClick={e => {
-        const rect = e.target.getBoundingClientRect();
-        setCoords({ x: e.clientX - rect.left, y: e.clientY - rect.top });
-        onClick && onClick(e);
-      }}
-    >
-      {isRippling ? (
-        <span
-          className="ripple"
-          style={{
-            left: coords.x,
-            top: coords.y
-          }}
-        />
-      ) : (
-        ''
-      )}
-      <span className="content">{children}</span>
+    <button onClick={clickHandler}>
+      {children}
+      {ripples}
     </button>
-  );
-};
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,39 +1,12 @@

 const RippleButton = ({ children, onClick }) => {
-  const [coords, setCoords] = React.useState({ x: -1, y: -1 });
-  const [isRippling, setIsRippling] = React.useState(false);
-
-  React.useEffect(() => {
-    if (coords.x !== -1 && coords.y !== -1) {
-      setIsRippling(true);
-      setTimeout(() => setIsRippling(false), 300);
-    } else setIsRippling(false);
-  }, [coords]);
-
-  React.useEffect(() => {
-    if (!isRippling) setCoords({ x: -1, y: -1 });
-  }, [isRippling]);
+  const handleClick = (e) => {
+    e.preventDefault();
+    onClick();
+  };
 
   return (
     <button
-      className="ripple-button"
-      onClick={e => {
-        const rect = e.target.getBoundingClientRect();
-        setCoords({ x: e.clientX - rect.left, y: e.clientY - rect.top });
-        onClick && onClick(e);
-      }}
+      onClick={handleClick}
+      className="border border-gray-400 hover:bg-gray-400 bg-transparent hover:text-gray-700 font-semibold hover:border-transparent rounded py-2 px-4"
     >
-      {isRippling ? (
-        <span
-          className="ripple"
-          style={{
-            left: coords.x,
-            top: coords.y
-          }}
-        />
-      ) : (
-        ''
-      )}
-      <span className="content">{children}</span>
-    </button>
-  );
-};
+      {
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,39 +1,13 @@

 const RippleButton = ({ children, onClick }) => {
-  const [coords, setCoords] = React.useState({ x: -1, y: -1 });
-  const [isRippling, setIsRippling] = React.useState(false);
+  const wrapperRef = useRef(null);
+  const [shouldBlur, setShouldBlur] = useState(false);
 
-  React.useEffect(() => {
-    if (coords.x !== -1 && coords.y !== -1) {
-      setIsRippling(true);
-      setTimeout(() => setIsRippling(false), 300);
-    } else setIsRippling(false);
-  }, [coords]);
+  const handleMouseDown = (e) => {
+    setShouldBlur(true);
+    e.persist();
+    e.stopPropagation();
+    e.nativeEvent.stopImmediatePropagation();
+  };
 
-  React.useEffect(() => {
-    if (!isRippling) setCoords({ x: -1, y: -1 });
-  }, [isRippling]);
-
-  return (
-    <button
-      className="ripple-button"
-      onClick={e => {
-        const rect = e.target.getBoundingClientRect();
-        setCoords({ x: e.clientX - rect.left, y: e.clientY - rect.top });
-        onClick && onClick(e);
-      }}
-    >
-      {isRippling ? (
-        <span
-          className="ripple"
-          style={{
-            left: coords.x,
-            top: coords.y
-          }}
-        />
-      ) : (
-        ''
-      )}
-      <span className="content">{children}</span>
-    </button>
-  );
-};
+  const handleMouseUp = (e) => {
+    set
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,39 +1,18 @@

 const RippleButton = ({ children, onClick }) => {
-  const [coords, setCoords] = React.useState({ x: -1, y: -1 });
-  const [isRippling, setIsRippling] = React.useState(false);
+  const [ripple, setRipple] = useState([]);
+  const classes = useStyles();
 
-  React.useEffect(() => {
-    if (coords.x !== -1 && coords.y !== -1) {
-      setIsRippling(true);
-      setTimeout(() => setIsRippling(false), 300);
-    } else setIsRippling(false);
-  }, [coords]);
+  const handleMouseDown = (event) => {
+    setRipple([
+      {
+        top: event.clientY,
+        left: event.clientX,
+      },
+    ]);
+  };
 
-  React.useEffect(() => {
-    if (!isRippling) setCoords({ x: -1, y: -1 });
-  }, [isRippling]);
+  const handleMouseUp = () => {
+    setRipple([]);
+  };
 
-  return (
-    <button
-      className="ripple-button"
-      onClick={e => {
-        const rect = e.target.getBoundingClientRect();
-        setCoords({ x: e.clientX - rect.left, y: e.clientY - rect.top });
-        onClick && onClick(e);
-      }}
-    >
-      {isRippling ? (
-        <span
-          className="ripple"
-          style={{
-            left: coords.x,
-            top: coords.y
-          }}
-        />
-      ) : (
-        ''
-      )}
-      <span className="content">{children}</span>
-    </button>
-  );
-};
+  const
```

### useMutationObserver (task/68)

#### canonical solution

```javascript
const useMutationObserver = (
  ref,
  callback,
  options = {
    attributes: true,
    characterData: true,
    childList: true,
    subtree: true,
  }
) => {
  React.useEffect(() => {
    if (ref.current) {
      const observer = new MutationObserver(callback);
      observer.observe(ref.current, options);
      return () => observer.disconnect();
    }
  }, [callback, options]);
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,17 +1,13 @@

-const useMutationObserver = (  ref,
-  callback,
-  options = {
-    attributes: true,
-    characterData: true,
-    childList: true,
-    subtree: true,
+const useMutationObserver = (() => {
+  const MutationObserver = (window as any).MutationObserver;
+  const isNative = MutationObserver !== undefined;
+  if (isNative) {
+    return () => {
+      const observer = new MutationObserver(callback);
+      return {
+        observe: observer.observe,
+        disconnect: observer.disconnect,
+      };
+    };
   }
-) => {
-  React.useEffect(() => {
-    if (ref.current) {
-      const observer = new MutationObserver(callback);
-      observer.observe(ref.current, options);
-      return () => observer.disconnect();
-    }
-  }, [callback, options]);
-};
+  const prefixes
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,17 +1,10 @@

-const useMutationObserver = (  ref,
-  callback,
-  options = {
-    attributes: true,
-    characterData: true,
-    childList: true,
-    subtree: true,
-  }
-) => {
-  React.useEffect(() => {
-    if (ref.current) {
-      const observer = new MutationObserver(callback);
-      observer.observe(ref.current, options);
-      return () => observer.disconnect();
-    }
-  }, [callback, options]);
-};
+const useMutationObserver = (): {
+  observe: (element: HTMLElement) => void;
+  disconnect: () => void;
+} => {
+  const observer = new MutationObserver(
+    (mutations) => {
+      mutations.forEach((mutation) => {
+        if (mutation.type === 'attributes') {
+          mutation.attributeName === 'data-name' &&
+            mutation.target.dispatchEvent(new Event
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,17 +1,11 @@

-const useMutationObserver = (  ref,
-  callback,
-  options = {
-    attributes: true,
-    characterData: true,
-    childList: true,
-    subtree: true,
-  }
-) => {
-  React.useEffect(() => {
-    if (ref.current) {
-      const observer = new MutationObserver(callback);
-      observer.observe(ref.current, options);
-      return () => observer.disconnect();
+const useMutationObserver = (callback: Function) => {
+  let observer: MutationObserver;
+  let fn: Function;
+  const callback2 = (mutations: MutationRecord[], observer: MutationObserver) => {
+    callback(mutations, observer);
+  };
+  const getObserver = () => {
+    if (!observer) {
+      observer = new MutationObserver(callback2);
     }
-  }, [callback, options]);
-};
+    return observer;
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,17 +1,12 @@

-const useMutationObserver = (  ref,
-  callback,
-  options = {
-    attributes: true,
-    characterData: true,
-    childList: true,
-    subtree: true,
-  }
-) => {
-  React.useEffect(() => {
-    if (ref.current) {
-      const observer = new MutationObserver(callback);
-      observer.observe(ref.current, options);
-      return () => observer.disconnect();
-    }
-  }, [callback, options]);
-};
+const useMutationObserver = (options) => {
+  const observers = new WeakMap();
+  return {
+    /**
+     * @function useMutationObserver
+     * @description callback will be called if element changes
+     * @param {HTMLElement} el
+     * @param {Function} cb
+     * @param {Object} options
+     * @returns {Object}
+     */
+    on: (el, cb, options) => {
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,17 +1,13 @@

-const useMutationObserver = (  ref,
-  callback,
-  options = {
-    attributes: true,
-    characterData: true,
-    childList: true,
-    subtree: true,
-  }
-) => {
-  React.useEffect(() => {
-    if (ref.current) {
-      const observer = new MutationObserver(callback);
-      observer.observe(ref.current, options);
-      return () => observer.disconnect();
-    }
-  }, [callback, options]);
+const useMutationObserver = (callback) => {
+    const observer = new MutationObserver(callback);
+    observer.observe(document.body, {
+        childList: true,
+        subtree: true,
+    });
 };
+
+export const useMutationObserverEffect = (callback) => {
+    useEffect(() => {
+        useMutationObserver(callback);
+    }, []);
+};
```

### Tooltip (task/69)

#### canonical solution

```javascript
const Tooltip = ({ children, text, ...rest }) => {
  const [show, setShow] = React.useState(false);

  return (
    <div className="tooltip-container">
      <div className={show ? 'tooltip-box visible' : 'tooltip-box'}>
        {text}
        <span className="tooltip-arrow" />
      </div>
      <div
        onMouseEnter={() => setShow(true)}
        onMouseLeave={() => setShow(false)}
        {...rest}
      >
        {children}
      </div>
    </div>
  );
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,19 +1,17 @@

 const Tooltip = ({ children, text, ...rest }) => {
-  const [show, setShow] = React.useState(false);
-
   return (
-    <div className="tooltip-container">
-      <div className={show ? 'tooltip-box visible' : 'tooltip-box'}>
-        {text}
-        <span className="tooltip-arrow" />
-      </div>
-      <div
-        onMouseEnter={() => setShow(true)}
-        onMouseLeave={() => setShow(false)}
-        {...rest}
-      >
-        {children}
-      </div>
-    </div>
+    <TooltipTrigger
+      mouseEnterDelay={0.1}
+      {...rest}
+    >
+      {children}
+      <TooltipContainer>
+        <TooltipArrow />
+        <TooltipText>{text}</TooltipText>
+      </TooltipContainer>
+    </TooltipTrigger>
   );
 };
+
+Tooltip.propTypes = {
+  children: PropTypes
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,19 +1,10 @@

 const Tooltip = ({ children, text, ...rest }) => {
-  const [show, setShow] = React.useState(false);
-
   return (
-    <div className="tooltip-container">
-      <div className={show ? 'tooltip-box visible' : 'tooltip-box'}>
-        {text}
-        <span className="tooltip-arrow" />
-      </div>
-      <div
-        onMouseEnter={() => setShow(true)}
-        onMouseLeave={() => setShow(false)}
-        {...rest}
-      >
-        {children}
-      </div>
-    </div>
+    <TooltipWrapper {...rest}>
+      {children}
+      <TooltipText>{text}</TooltipText>
+    </TooltipWrapper>
   );
 };
+
+export default Tooltip;
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,19 +1,15 @@

 const Tooltip = ({ children, text, ...rest }) => {
-  const [show, setShow] = React.useState(false);
-
   return (
-    <div className="tooltip-container">
-      <div className={show ? 'tooltip-box visible' : 'tooltip-box'}>
-        {text}
-        <span className="tooltip-arrow" />
-      </div>
-      <div
-        onMouseEnter={() => setShow(true)}
-        onMouseLeave={() => setShow(false)}
-        {...rest}
-      >
-        {children}
-      </div>
-    </div>
+    <TooltipWrapper {...rest}>
+      {children}
+      <TooltipText>{text}</TooltipText>
+    </TooltipWrapper>
   );
 };
+
+Tooltip.propTypes = {
+  children: PropTypes.node.isRequired,
+  text: PropTypes.string.isRequired,
+};
+
+export default Tooltip;
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,19 +1,15 @@

 const Tooltip = ({ children, text, ...rest }) => {
-  const [show, setShow] = React.useState(false);
-
   return (
-    <div className="tooltip-container">
-      <div className={show ? 'tooltip-box visible' : 'tooltip-box'}>
-        {text}
-        <span className="tooltip-arrow" />
-      </div>
-      <div
-        onMouseEnter={() => setShow(true)}
-        onMouseLeave={() => setShow(false)}
-        {...rest}
-      >
-        {children}
-      </div>
-    </div>
+    <TooltipEl {...rest}>
+      {children}
+      <span>{text}</span>
+    </TooltipEl>
   );
 };
+
+Tooltip.propTypes = {
+  children: PropTypes.node.isRequired,
+  text: PropTypes.string.isRequired,
+};
+
+export default Tooltip;
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,19 +1,18 @@

 const Tooltip = ({ children, text, ...rest }) => {
-  const [show, setShow] = React.useState(false);
-
   return (
-    <div className="tooltip-container">
-      <div className={show ? 'tooltip-box visible' : 'tooltip-box'}>
-        {text}
-        <span className="tooltip-arrow" />
-      </div>
-      <div
-        onMouseEnter={() => setShow(true)}
-        onMouseLeave={() => setShow(false)}
-        {...rest}
-      >
-        {children}
-      </div>
-    </div>
+    <TooltipWrapper
+      className="tooltip"
+      tooltip={text}
+      {...rest}
+    >
+      {children}
+    </TooltipWrapper>
   );
 };
+
+Tooltip.propTypes = {
+  children: PropTypes.node.isRequired,
+  text: PropTypes.string.isRequired,
+};
+
+export default Tooltip;
```

### useTimeout (task/70)

#### canonical solution

```javascript
const useTimeout = (callback, delay) => {
  const savedCallback = React.useRef();

  React.useEffect(() => {
    savedCallback.current = callback;
  }, [callback]);

  React.useEffect(() => {
    const tick = () => {
      savedCallback.current();
    }
    if (delay !== null) {
      let id = setTimeout(tick, delay);
      return () => clearTimeout(id);
    }
  }, [delay]);
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,17 +1,16 @@

 const useTimeout = (callback, delay) => {
-  const savedCallback = React.useRef();
+  const savedCallback = useRef();
 
-  React.useEffect(() => {
+  // Remember the latest callback.
+  useEffect(() => {
     savedCallback.current = callback;
   }, [callback]);
 
-  React.useEffect(() => {
-    const tick = () => {
+  // Set up the interval.
+  useEffect(() => {
+    function tick() {
       savedCallback.current();
     }
     if (delay !== null) {
-      let id = setTimeout(tick, delay);
-      return () => clearTimeout(id);
-    }
-  }, [delay]);
-};
+      let id = setInterval(tick, delay);
+      return ()
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,17 +1,16 @@

 const useTimeout = (callback, delay) => {
-  const savedCallback = React.useRef();
+  const savedCallback = useRef();
 
-  React.useEffect(() => {
+  // Remember the latest callback.
+  useEffect(() => {
     savedCallback.current = callback;
   }, [callback]);
 
-  React.useEffect(() => {
-    const tick = () => {
+  // Set up the interval.
+  useEffect(() => {
+    function tick() {
       savedCallback.current();
     }
     if (delay !== null) {
-      let id = setTimeout(tick, delay);
-      return () => clearTimeout(id);
-    }
-  }, [delay]);
-};
+      let id = setInterval(tick, delay);
+      return ()
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,17 +1,16 @@

 const useTimeout = (callback, delay) => {
-  const savedCallback = React.useRef();
+  const savedCallback = useRef();
 
-  React.useEffect(() => {
+  // Remember the latest callback.
+  useEffect(() => {
     savedCallback.current = callback;
   }, [callback]);
 
-  React.useEffect(() => {
-    const tick = () => {
+  // Set up the interval.
+  useEffect(() => {
+    function tick() {
       savedCallback.current();
     }
     if (delay !== null) {
-      let id = setTimeout(tick, delay);
-      return () => clearTimeout(id);
-    }
-  }, [delay]);
-};
+      let id = setInterval(tick, delay);
+      return ()
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,17 +1,16 @@

 const useTimeout = (callback, delay) => {
-  const savedCallback = React.useRef();
+  const savedCallback = useRef();
 
-  React.useEffect(() => {
+  // Remember the latest callback.
+  useEffect(() => {
     savedCallback.current = callback;
   }, [callback]);
 
-  React.useEffect(() => {
-    const tick = () => {
+  // Set up the interval.
+  useEffect(() => {
+    function tick() {
       savedCallback.current();
     }
     if (delay !== null) {
-      let id = setTimeout(tick, delay);
-      return () => clearTimeout(id);
-    }
-  }, [delay]);
-};
+      let id = setInterval(tick, delay);
+      return ()
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,17 +1,16 @@

 const useTimeout = (callback, delay) => {
-  const savedCallback = React.useRef();
+  const savedCallback = useRef();
 
-  React.useEffect(() => {
+  // Remember the latest callback.
+  useEffect(() => {
     savedCallback.current = callback;
   }, [callback]);
 
-  React.useEffect(() => {
-    const tick = () => {
+  // Set up the interval.
+  useEffect(() => {
+    function tick() {
       savedCallback.current();
     }
     if (delay !== null) {
-      let id = setTimeout(tick, delay);
-      return () => clearTimeout(id);
-    }
-  }, [delay]);
-};
+      let id = setInterval(tick, delay);
+      return ()
```

### useError (task/71)

#### canonical solution

```javascript
const useError = err => {
  const [error, setError] = React.useState(err);

  React.useEffect(() => {
    if (error) throw error;
  }, [error]);

  const dispatchError = React.useCallback(err => {
    setError(err);
  }, []);

  return dispatchError;
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,13 +1,13 @@

 const useError = err => {
-  const [error, setError] = React.useState(err);
+  return {
+    type: ERROR,
+    payload: err
+  };
+};
 
-  React.useEffect(() => {
-    if (error) throw error;
-  }, [error]);
-
-  const dispatchError = React.useCallback(err => {
-    setError(err);
-  }, []);
-
-  return dispatchError;
+export const useErrorActions = () => {
+  const dispatch = useDispatch();
+  return {
+    setError: (err: string) => dispatch(useError(err))
+  };
 };
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,13 +1,11 @@

 const useError = err => {
-  const [error, setError] = React.useState(err);
+  console.log(err);
+  return true;
+};
 
-  React.useEffect(() => {
-    if (error) throw error;
-  }, [error]);
-
-  const dispatchError = React.useCallback(err => {
-    setError(err);
-  }, []);
-
-  return dispatchError;
-};
+const getData = async (address, month, year) => {
+  try {
+    const response = await fetch(
+      `https://www.nemlig.com/nemlig/api/v1/rest/mandel?address=${address}&month=${month}&year=${year}`
+    );
+    const result = await response.
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,13 +1,15 @@

 const useError = err => {
-  const [error, setError] = React.useState(err);
+  const [errorMessage, setErrorMessage] = useState(err);
+  const [errorStatus, setErrorStatus] = useState(null);
 
-  React.useEffect(() => {
-    if (error) throw error;
-  }, [error]);
+  useEffect(() => {
+    if (err) {
+      setErrorMessage(err.message);
+      setErrorStatus(err.status);
+    }
+  }, [err]);
 
-  const dispatchError = React.useCallback(err => {
-    setError(err);
-  }, []);
+  return { errorMessage, errorStatus };
+};
 
-  return dispatchError;
-};
+export default useError;
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,13 +1,6 @@

 const useError = err => {
-  const [error, setError] = React.useState(err);
+  const [error, setError] = useState(err);
+  return [error, setError];
+};
 
-  React.useEffect(() => {
-    if (error) throw error;
-  }, [error]);
-
-  const dispatchError = React.useCallback(err => {
-    setError(err);
-  }, []);
-
-  return dispatchError;
-};
+export default useError;
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,13 +1,12 @@

 const useError = err => {
-  const [error, setError] = React.useState(err);
+  const [error, setError] = useState<string>(err);
+  return [error, setError];
+};
 
-  React.useEffect(() => {
-    if (error) throw error;
-  }, [error]);
+const useLoading = () => {
+  const [loading, setLoading] = useState<boolean>(false);
+  return [loading, setLoading];
+};
 
-  const dispatchError = React.useCallback(err => {
-    setError(err);
-  }, []);
-
-  return dispatchError;
-};
+const useLoadingSpinner = (loading: boolean) => {
+  const [showSpinner, setShowSpinner] = useState<bo
```

### useCopyToClipboard (task/72)

#### canonical solution

```javascript
const useCopyToClipboard = text => {
  const copyToClipboard = str => {
    const el = document.createElement('textarea');
    el.value = str;
    el.setAttribute('readonly', '');
    el.style.position = 'absolute';
    el.style.left = '-9999px';
    document.body.appendChild(el);
    const selected =
      document.getSelection().rangeCount > 0
        ? document.getSelection().getRangeAt(0)
        : false;
    el.select();
    const success = document.execCommand('copy');
    document.body.removeChild(el);
    if (selected) {
      document.getSelection().removeAllRanges();
      document.getSelection().addRange(selected);
    }
    return success;
  };

  const [copied, setCopied] = React.useState(false);

  const copy = React.useCallback(() => {
    if (!copied) setCopied(copyToClipboard(text));
  }, [text]);
  React.useEffect(() => () => setCopied(false), [text]);

  return [copied, copy];
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,31 +1,12 @@

 const useCopyToClipboard = text => {
-  const copyToClipboard = str => {
-    const el = document.createElement('textarea');
-    el.value = str;
-    el.setAttribute('readonly', '');
-    el.style.position = 'absolute';
-    el.style.left = '-9999px';
-    document.body.appendChild(el);
-    const selected =
-      document.getSelection().rangeCount > 0
-        ? document.getSelection().getRangeAt(0)
-        : false;
-    el.select();
-    const success = document.execCommand('copy');
-    document.body.removeChild(el);
-    if (selected) {
-      document.getSelection().removeAllRanges();
-      document.getSelection().addRange(selected);
-    }
-    return success;
+  const [copied, setCopied] = useState(false);
+  const handleClick = () => {
+    setCopied(true);
+    copy(text);
+    setTimeout(() => setCopied(false), 1000);
   };
+  return [copied, handleClick];
+};
 
-  const [copied, setCopied] = React.useState(false);
-
-  const copy = React.useCallback(() => {
-    if (!copied) setCopied(copyToClipboard(text));
-  }, [text]);
-  React.useEffect(() => () => setCopied(false), [text]);
-
-  return [copied, copy];
-};
+const CopyLink = ({ text }) => {
+  const [copied, handleClick] = useCopyToClipboard(
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,31 +1,14 @@

 const useCopyToClipboard = text => {
-  const copyToClipboard = str => {
-    const el = document.createElement('textarea');
-    el.value = str;
-    el.setAttribute('readonly', '');
-    el.style.position = 'absolute';
-    el.style.left = '-9999px';
-    document.body.appendChild(el);
-    const selected =
-      document.getSelection().rangeCount > 0
-        ? document.getSelection().getRangeAt(0)
-        : false;
-    el.select();
-    const success = document.execCommand('copy');
-    document.body.removeChild(el);
-    if (selected) {
-      document.getSelection().removeAllRanges();
-      document.getSelection().addRange(selected);
-    }
-    return success;
-  };
+  const [hasCopied, setHasCopied] = useState(false);
 
-  const [copied, setCopied] = React.useState(false);
+  const copyToClipboard = useCallback(() => {
+    if (hasCopied) return;
 
-  const copy = React.useCallback(() => {
-    if (!copied) setCopied(copyToClipboard(text));
-  }, [text]);
-  React.useEffect(() => () => setCopied(false), [text]);
+    navigator.clipboard.writeText(text);
+    setHasCopied(true);
 
-  return [copied, copy];
-};
+    setTimeout(() => {
+      setHasCopied(false);
+    }, 2000);
+  }, [text, hasCopied]);
+
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,31 +1,13 @@

 const useCopyToClipboard = text => {
-  const copyToClipboard = str => {
-    const el = document.createElement('textarea');
-    el.value = str;
-    el.setAttribute('readonly', '');
-    el.style.position = 'absolute';
-    el.style.left = '-9999px';
-    document.body.appendChild(el);
-    const selected =
-      document.getSelection().rangeCount > 0
-        ? document.getSelection().getRangeAt(0)
-        : false;
-    el.select();
-    const success = document.execCommand('copy');
-    document.body.removeChild(el);
-    if (selected) {
-      document.getSelection().removeAllRanges();
-      document.getSelection().addRange(selected);
-    }
-    return success;
+  const [isLoading, setIsLoading] = useState(false);
+  const [isCopied, setIsCopied] = useState(false);
+
+  const copyToClipboard = () => {
+    setIsLoading(true);
+    setIsCopied(true);
+    setTimeout(() => {
+      setIsCopied(false);
+      setIsLoading(false);
+    }, 1500);
   };
 
-  const [copied, setCopied] = React.useState(false);
-
-  const copy = React.useCallback(() => {
-    if (!copied) setCopied(copyToClipboard(text));
-  }, [text]);
-  React.useEffect(() => () => setCopied(false), [text]);
-
-  return [copied, copy];
-};
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,31 +1,15 @@

 const useCopyToClipboard = text => {
-  const copyToClipboard = str => {
-    const el = document.createElement('textarea');
-    el.value = str;
-    el.setAttribute('readonly', '');
-    el.style.position = 'absolute';
-    el.style.left = '-9999px';
-    document.body.appendChild(el);
-    const selected =
-      document.getSelection().rangeCount > 0
-        ? document.getSelection().getRangeAt(0)
-        : false;
-    el.select();
-    const success = document.execCommand('copy');
-    document.body.removeChild(el);
-    if (selected) {
-      document.getSelection().removeAllRanges();
-      document.getSelection().addRange(selected);
-    }
-    return success;
-  };
+  const [hasCopied, setHasCopied] = useState(false);
 
-  const [copied, setCopied] = React.useState(false);
+  const copyToClipboard = useCallback(() => {
+    if (hasCopied) return;
 
-  const copy = React.useCallback(() => {
-    if (!copied) setCopied(copyToClipboard(text));
-  }, [text]);
-  React.useEffect(() => () => setCopied(false), [text]);
+    copy(text);
+    setHasCopied(true);
 
-  return [copied, copy];
-};
+    setTimeout(() => {
+      setHasCopied(false);
+    }, 2000);
+  }, [hasCopied, text]);
+
+  return [copyToClip
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,31 +1,12 @@

 const useCopyToClipboard = text => {
-  const copyToClipboard = str => {
-    const el = document.createElement('textarea');
-    el.value = str;
-    el.setAttribute('readonly', '');
-    el.style.position = 'absolute';
-    el.style.left = '-9999px';
-    document.body.appendChild(el);
-    const selected =
-      document.getSelection().rangeCount > 0
-        ? document.getSelection().getRangeAt(0)
-        : false;
-    el.select();
-    const success = document.execCommand('copy');
-    document.body.removeChild(el);
-    if (selected) {
-      document.getSelection().removeAllRanges();
-      document.getSelection().addRange(selected);
-    }
-    return success;
-  };
+	const [isCopied, setIsCopied] = useState(false);
 
-  const [copied, setCopied] = React.useState(false);
+	const onCopy = () => {
+		setIsCopied(true);
+		setTimeout(() => setIsCopied(false), 2000);
+	};
 
-  const copy = React.useCallback(() => {
-    if (!copied) setCopied(copyToClipboard(text));
-  }, [text]);
-  React.useEffect(() => () => setCopied(false), [text]);
+	return [isCopied, onCopy, text];
+};
 
-  return [copied, copy];
-};
+export default useCopyToClipboard;
```

### useMap (task/73)

#### canonical solution

```javascript
const useMap = initialValue => {
  const [map, setMap] = React.useState(new Map(initialValue));

  const actions = React.useMemo(
    () => ({
      set: (key, value) =>
        setMap(prevMap => {
          const nextMap = new Map(prevMap);
          nextMap.set(key, value);
          return nextMap;
        }),
      remove: (key, value) =>
        setMap(prevMap => {
          const nextMap = new Map(prevMap);
          nextMap.delete(key, value);
          return nextMap;
        }),
      clear: () => setMap(new Map()),
    }),
    [setMap]
  );

  return [map, actions];
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,24 +1,14 @@

 const useMap = initialValue => {
-  const [map, setMap] = React.useState(new Map(initialValue));
+  const [map, setMap] = useState(initialValue);
 
-  const actions = React.useMemo(
-    () => ({
-      set: (key, value) =>
-        setMap(prevMap => {
-          const nextMap = new Map(prevMap);
-          nextMap.set(key, value);
-          return nextMap;
-        }),
-      remove: (key, value) =>
-        setMap(prevMap => {
-          const nextMap = new Map(prevMap);
-          nextMap.delete(key, value);
-          return nextMap;
-        }),
-      clear: () => setMap(new Map()),
-    }),
-    [setMap]
-  );
+  const updateMap = (key, value) => {
+    setMap({
+      ...map,
+      [key]: value,
+    });
+  };
 
-  return [map, actions];
+  return [map, updateMap];
 };
+
+export default useMap;
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,24 +1,10 @@

 const useMap = initialValue => {
-  const [map, setMap] = React.useState(new Map(initialValue));
+  const [state, setState] = useState(initialValue);
+  const set = key => value => setState({ ...state, [key]: value });
+  return [state, set];
+};
 
-  const actions = React.useMemo(
-    () => ({
-      set: (key, value) =>
-        setMap(prevMap => {
-          const nextMap = new Map(prevMap);
-          nextMap.set(key, value);
-          return nextMap;
-        }),
-      remove: (key, value) =>
-        setMap(prevMap => {
-          const nextMap = new Map(prevMap);
-          nextMap.delete(key, value);
-          return nextMap;
-        }),
-      clear: () => setMap(new Map()),
-    }),
-    [setMap]
-  );
-
-  return [map, actions];
-};
+const Person = ({ name, onChange, onRemove }) => {
+  const [nameState, setName] = useMap(name);
+  const [ageState, setAge] = useMap('');
+  const [gender
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,24 +1,9 @@

 const useMap = initialValue => {
-  const [map, setMap] = React.useState(new Map(initialValue));
+  const [state, setState] = useState(initialValue);
+  const setMap = useCallback(newState => {
+    setState(newState);
+  }, []);
+  return [state, setMap];
+};
 
-  const actions = React.useMemo(
-    () => ({
-      set: (key, value) =>
-        setMap(prevMap => {
-          const nextMap = new Map(prevMap);
-          nextMap.set(key, value);
-          return nextMap;
-        }),
-      remove: (key, value) =>
-        setMap(prevMap => {
-          const nextMap = new Map(prevMap);
-          nextMap.delete(key, value);
-          return nextMap;
-        }),
-      clear: () => setMap(new Map()),
-    }),
-    [setMap]
-  );
-
-  return [map, actions];
-};
+export default useMap;
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,24 +1,15 @@

 const useMap = initialValue => {
-  const [map, setMap] = React.useState(new Map(initialValue));
-
-  const actions = React.useMemo(
-    () => ({
-      set: (key, value) =>
-        setMap(prevMap => {
-          const nextMap = new Map(prevMap);
-          nextMap.set(key, value);
-          return nextMap;
-        }),
-      remove: (key, value) =>
-        setMap(prevMap => {
-          const nextMap = new Map(prevMap);
-          nextMap.delete(key, value);
-          return nextMap;
-        }),
-      clear: () => setMap(new Map()),
-    }),
-    [setMap]
-  );
-
-  return [map, actions];
-};
+  const map = new Map(initialValue);
+  const get = index => {
+    return map.get(index);
+  };
+  const set = (index, value) => {
+    map.set(index, value);
+  };
+  const has = index => {
+    return map.has(index);
+  };
+  const remove = index => {
+    map.delete(index);
+  };
+  const keys
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,24 +1,9 @@

 const useMap = initialValue => {
-  const [map, setMap] = React.useState(new Map(initialValue));
+    const [state, setState] = useState(initialValue);
+    const setData = data => {
+        setState(data);
+    };
+    return [state, setData];
+};
 
-  const actions = React.useMemo(
-    () => ({
-      set: (key, value) =>
-        setMap(prevMap => {
-          const nextMap = new Map(prevMap);
-          nextMap.set(key, value);
-          return nextMap;
-        }),
-      remove: (key, value) =>
-        setMap(prevMap => {
-          const nextMap = new Map(prevMap);
-          nextMap.delete(key, value);
-          return nextMap;
-        }),
-      clear: () => setMap(new Map()),
-    }),
-    [setMap]
-  );
-
-  return [map, actions];
-};
+export default useMap;
```

### AutoLink (task/74)

#### canonical solution

```javascript
const AutoLink = ({ text }) => {
  const delimiter = /((?:https?:\/\/)?(?:(?:[a-z0-9]?(?:[a-z0-9\-]{1,61}[a-z0-9])?\.[^\.|\s])+[a-z\.]*[a-z]+|(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3})(?::\d{1,5})*[a-z0-9.,_\/~#&=;%+?\-\\(\\)]*)/gi;

  return (
    <>
      {text.split(delimiter).map(word => {
        const match = word.match(delimiter);
        if (match) {
          const url = match[0];
          return (
            <a href={url.startsWith('http') ? url : `http://${url}`}>{url}</a>
          );
        }
        return word;
      })}
    </>
  );
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,18 +1,12 @@

 const AutoLink = ({ text }) => {
-  const delimiter = /((?:https?:\/\/)?(?:(?:[a-z0-9]?(?:[a-z0-9\-]{1,61}[a-z0-9])?\.[^\.|\s])+[a-z\.]*[a-z]+|(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3})(?::\d{1,5})*[a-z0-9.,_\/~#&=;%+?\-\\(\\)]*)/gi;
+  const result = reactLinkify({
+    target: '_blank',
+    className: '',
+    componentDecorator: (decoratedHref, decoratedText, key) => (
+      <span key={key}>
+        <a href={decoratedHref}>{decoratedText}</a>
+      </span>
+    ),
+  })(text);
 
-  return (
-    <>
-      {text.split(delimiter).map(word => {
-        const match = word.match(delimiter);
-        if (match) {
-          const url = match[0];
-          return (
-            <a href={url.startsWith('http') ? url : `http://${url}`}>{url}</a>
-          );
-        }
-        return word;
-      })}
-    </>
-  );
-};
+  return <React.Fragment
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,18 +1,11 @@

 const AutoLink = ({ text }) => {
-  const delimiter = /((?:https?:\/\/)?(?:(?:[a-z0-9]?(?:[a-z0-9\-]{1,61}[a-z0-9])?\.[^\.|\s])+[a-z\.]*[a-z]+|(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3})(?::\d{1,5})*[a-z0-9.,_\/~#&=;%+?\-\\(\\)]*)/gi;
-
   return (
     <>
-      {text.split(delimiter).map(word => {
-        const match = word.match(delimiter);
-        if (match) {
-          const url = match[0];
-          return (
-            <a href={url.startsWith('http') ? url : `http://${url}`}>{url}</a>
-          );
-        }
-        return word;
-      })}
+      <a href={text} className="underline text-blue-600 hover:text-blue-600 no-underline">
+        {text}
+      </a>
     </>
   );
 };
+
+export default AutoLink;
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,18 +1,6 @@

 const AutoLink = ({ text }) => {
-  const delimiter = /((?:https?:\/\/)?(?:(?:[a-z0-9]?(?:[a-z0-9\-]{1,61}[a-z0-9])?\.[^\.|\s])+[a-z\.]*[a-z]+|(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3})(?::\d{1,5})*[a-z0-9.,_\/~#&=;%+?\-\\(\\)]*)/gi;
+  const autoLink = useAutoLink(text);
+  return <Text>{autoLink}</Text>;
+};
 
-  return (
-    <>
-      {text.split(delimiter).map(word => {
-        const match = word.match(delimiter);
-        if (match) {
-          const url = match[0];
-          return (
-            <a href={url.startsWith('http') ? url : `http://${url}`}>{url}</a>
-          );
-        }
-        return word;
-      })}
-    </>
-  );
-};
+export default AutoLink;
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,18 +1,12 @@

 const AutoLink = ({ text }) => {
-  const delimiter = /((?:https?:\/\/)?(?:(?:[a-z0-9]?(?:[a-z0-9\-]{1,61}[a-z0-9])?\.[^\.|\s])+[a-z\.]*[a-z]+|(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3})(?::\d{1,5})*[a-z0-9.,_\/~#&=;%+?\-\\(\\)]*)/gi;
+  const [isClicked, setIsClicked] = useState(false);
+  const [state, setState] = useState({
+    data: [],
+    isLoading: false,
+    isError: false,
+  });
 
-  return (
-    <>
-      {text.split(delimiter).map(word => {
-        const match = word.match(delimiter);
-        if (match) {
-          const url = match[0];
-          return (
-            <a href={url.startsWith('http') ? url : `http://${url}`}>{url}</a>
-          );
-        }
-        return word;
-      })}
-    </>
-  );
-};
+  const checkForUnclicked = () => {
+    if (isClicked) {
+      const array = state.data.filter((item) => item.text === text);
+      if
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,18 +1,8 @@

 const AutoLink = ({ text }) => {
-  const delimiter = /((?:https?:\/\/)?(?:(?:[a-z0-9]?(?:[a-z0-9\-]{1,61}[a-z0-9])?\.[^\.|\s])+[a-z\.]*[a-z]+|(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3})(?::\d{1,5})*[a-z0-9.,_\/~#&=;%+?\-\\(\\)]*)/gi;
-
+  const link = 'https://github.com/nireo/generator-nextjs';
   return (
-    <>
-      {text.split(delimiter).map(word => {
-        const match = word.match(delimiter);
-        if (match) {
-          const url = match[0];
-          return (
-            <a href={url.startsWith('http') ? url : `http://${url}`}>{url}</a>
-          );
-        }
-        return word;
-      })}
-    </>
-  );
-};
+    <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-sm font-medium leading-5 bg-orange-200 text-orange-800">
+      {text}
+      <span className="ml-1.5">
+        <svg
+         
```

### useDebounce (task/75)

#### canonical solution

```javascript
const useDebounce = (value, delay) => {
  const [debouncedValue, setDebouncedValue] = React.useState(value);

  React.useEffect(() => {
    const handler = setTimeout(() => {
      setDebouncedValue(value);
    }, delay);

    return () => {
      clearTimeout(handler);
    };
  }, [value]);

  return debouncedValue;
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,7 +1,7 @@

 const useDebounce = (value, delay) => {
-  const [debouncedValue, setDebouncedValue] = React.useState(value);
+  const [debouncedValue, setDebouncedValue] = useState(value);
 
-  React.useEffect(() => {
+  useEffect(() => {
     const handler = setTimeout(() => {
       setDebouncedValue(value);
     }, delay);
@@ -9,7 +9,9 @@

     return () => {
       clearTimeout(handler);
     };
-  }, [value]);
+  }, [value, delay]);
 
   return debouncedValue;
 };
+
+export default useDebounce;
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,7 +1,7 @@

 const useDebounce = (value, delay) => {
-  const [debouncedValue, setDebouncedValue] = React.useState(value);
+  const [debouncedValue, setDebouncedValue] = useState(value);
 
-  React.useEffect(() => {
+  useEffect(() => {
     const handler = setTimeout(() => {
       setDebouncedValue(value);
     }, delay);
@@ -9,7 +9,9 @@

     return () => {
       clearTimeout(handler);
     };
-  }, [value]);
+  }, [value, delay]);
 
   return debouncedValue;
 };
+
+const Search = ({ searchUsers, clearUsers, showClear
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,7 +1,7 @@

 const useDebounce = (value, delay) => {
-  const [debouncedValue, setDebouncedValue] = React.useState(value);
+  const [debouncedValue, setDebouncedValue] = useState(value);
 
-  React.useEffect(() => {
+  useEffect(() => {
     const handler = setTimeout(() => {
       setDebouncedValue(value);
     }, delay);
@@ -9,7 +9,9 @@

     return () => {
       clearTimeout(handler);
     };
-  }, [value]);
+  }, [value, delay]);
 
   return debouncedValue;
 };
+
+export default useDebounce;
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,15 +1,17 @@

 const useDebounce = (value, delay) => {
-  const [debouncedValue, setDebouncedValue] = React.useState(value);
+    const [debouncedValue, setDebouncedValue] = useState(value);
 
-  React.useEffect(() => {
-    const handler = setTimeout(() => {
-      setDebouncedValue(value);
-    }, delay);
+    useEffect(() => {
+        const handler = setTimeout(() => {
+            setDebouncedValue(value);
+        }, delay);
 
-    return () => {
-      clearTimeout(handler);
-    };
-  }, [value]);
+        return () => {
+            clearTimeout(handler);
+        };
+    }, [value, delay]);
 
-  return debouncedValue;
+    return debouncedValue;
 };
+
+export default useDebounce;
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,7 +1,7 @@

 const useDebounce = (value, delay) => {
-  const [debouncedValue, setDebouncedValue] = React.useState(value);
+  const [debouncedValue, setDebouncedValue] = useState(value);
 
-  React.useEffect(() => {
+  useEffect(() => {
     const handler = setTimeout(() => {
       setDebouncedValue(value);
     }, delay);
@@ -9,7 +9,9 @@

     return () => {
       clearTimeout(handler);
     };
-  }, [value]);
+  }, [value, delay]);
 
   return debouncedValue;
 };
+
+export default useDebounce;
```

### useFetch (task/76)

#### canonical solution

```javascript
const useFetch = (url, options) => {
  const [response, setResponse] = React.useState(null);
  const [error, setError] = React.useState(null);

  React.useEffect(() => {
    const fetchData = async () => {
      try {
        const res = await fetch(url, options);
        const json = await res.json();
        setResponse(json);
      } catch (error) {
        setError(error);
      }
    };
    fetchData();
  }, []);

  return { response, error };
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,19 +1,11 @@

 const useFetch = (url, options) => {
-  const [response, setResponse] = React.useState(null);
-  const [error, setError] = React.useState(null);
+  const [response, setResponse] = useState(null);
+  const [error, setError] = useState(null);
+  const [isLoading, setIsLoading] = useState(false);
 
-  React.useEffect(() => {
+  useEffect(() => {
     const fetchData = async () => {
+      setIsLoading(true);
       try {
         const res = await fetch(url, options);
         const json = await res.json();
-        setResponse(json);
-      } catch (error) {
-        setError(error);
-      }
-    };
-    fetchData();
-  }, []);
-
-  return { response, error };
-};
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,19 +1,13 @@

 const useFetch = (url, options) => {
-  const [response, setResponse] = React.useState(null);
-  const [error, setError] = React.useState(null);
+  const [data, setData] = useState(null);
+  const [loading, setLoading] = useState(true);
+  const [error, setError] = useState(null);
 
-  React.useEffect(() => {
-    const fetchData = async () => {
-      try {
-        const res = await fetch(url, options);
-        const json = await res.json();
-        setResponse(json);
-      } catch (error) {
-        setError(error);
-      }
-    };
-    fetchData();
-  }, []);
+  useEffect(() => {
+    setLoading(true);
+    setError(null);
 
-  return { response, error };
-};
+    fetch(url, options)
+      .then(res => {
+        if (!res.ok) {
+          throw new Error(res
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,19 +1,12 @@

 const useFetch = (url, options) => {
-  const [response, setResponse] = React.useState(null);
-  const [error, setError] = React.useState(null);
+  const [data, setData] = useState(null);
+  const [loading, setLoading] = useState(true);
+  const [error, setError] = useState(null);
 
-  React.useEffect(() => {
+  useEffect(() => {
     const fetchData = async () => {
       try {
         const res = await fetch(url, options);
         const json = await res.json();
-        setResponse(json);
-      } catch (error) {
-        setError(error);
-      }
-    };
-    fetchData();
-  }, []);
-
-  return { response, error };
-};
+        setData(json);
+        set
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,19 +1,12 @@

 const useFetch = (url, options) => {
-  const [response, setResponse] = React.useState(null);
-  const [error, setError] = React.useState(null);
+  const [data, setData] = useState({})
+  const [loading, setLoading] = useState(true)
+  const [error, setError] = useState(null)
 
-  React.useEffect(() => {
+  useEffect(() => {
     const fetchData = async () => {
       try {
-        const res = await fetch(url, options);
-        const json = await res.json();
-        setResponse(json);
-      } catch (error) {
-        setError(error);
-      }
-    };
-    fetchData();
-  }, []);
-
-  return { response, error };
-};
+        const response = await fetch(url, options)
+        const data = await response.json()
+        setData(data)
+        setLoading
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,19 +1,12 @@

 const useFetch = (url, options) => {
-  const [response, setResponse] = React.useState(null);
-  const [error, setError] = React.useState(null);
+    const [data, setData] = useState(null);
+    const [loading, setLoading] = useState(true);
+    const [error, setError] = useState(null);
 
-  React.useEffect(() => {
-    const fetchData = async () => {
-      try {
-        const res = await fetch(url, options);
-        const json = await res.json();
-        setResponse(json);
-      } catch (error) {
-        setError(error);
-      }
-    };
-    fetchData();
-  }, []);
-
-  return { response, error };
-};
+    useEffect(() => {
+        setLoading(true);
+        fetch(url, options)
+            .then(res => res.json())
+            .then(json => {
+                setData(json);
+                setLoading(
```

### useOnGlobalEvent (task/77)

#### canonical solution

```javascript
const useOnGlobalEvent = (type, callback, options) => {
  const listener = React.useRef(null);
  const previousProps = React.useRef({ type, options });

  React.useEffect(() => {
    const { type: previousType, options: previousOptions } = previousProps;

    if (listener.current) {
      window.removeEventListener(
        previousType,
        listener.current,
        previousOptions
      );
    }

    listener.current = window.addEventListener(type, callback, options);
    previousProps.current = { type, options };

    return () => {
      window.removeEventListener(type, listener.current, options);
    };
  }, [callback, type, options]);
};
```

#### solution 0

```diff
--- canonical.py

+++ solution0.py

@@ -1,23 +1,10 @@

 const useOnGlobalEvent = (type, callback, options) => {
-  const listener = React.useRef(null);
-  const previousProps = React.useRef({ type, options });
+  useEffect(() => {
+    window.addEventListener(type, callback, options);
+    return () => {
+      window.removeEventListener(type, callback, options);
+    };
+  }, [type, callback, options]);
+};
 
-  React.useEffect(() => {
-    const { type: previousType, options: previousOptions } = previousProps;
-
-    if (listener.current) {
-      window.removeEventListener(
-        previousType,
-        listener.current,
-        previousOptions
-      );
-    }
-
-    listener.current = window.addEventListener(type, callback, options);
-    previousProps.current = { type, options };
-
-    return () => {
-      window.removeEventListener(type, listener.current, options);
-    };
-  }, [callback, type, options]);
-};
+export default useOnGlobalEvent;
```

#### solution 1

```diff
--- canonical.py

+++ solution1.py

@@ -1,23 +1,12 @@

 const useOnGlobalEvent = (type, callback, options) => {
-  const listener = React.useRef(null);
-  const previousProps = React.useRef({ type, options });
+  return eventEmitter.on(type, callback, options);
+};
 
-  React.useEffect(() => {
-    const { type: previousType, options: previousOptions } = previousProps;
-
-    if (listener.current) {
-      window.removeEventListener(
-        previousType,
-        listener.current,
-        previousOptions
-      );
-    }
-
-    listener.current = window.addEventListener(type, callback, options);
-    previousProps.current = { type, options };
-
-    return () => {
-      window.removeEventListener(type, listener.current, options);
-    };
-  }, [callback, type, options]);
-};
+export const useOnType = (type, options) => {
+  const [emitter] = useGlobalEvent(type);
+  const on = useCallback(() => {
+    emitter.on(type, () => options.callback(type));
+  }, [type, options]);
+  useEffect(() => {
+    on();
+  }, [on
```

#### solution 2

```diff
--- canonical.py

+++ solution2.py

@@ -1,23 +1,16 @@

 const useOnGlobalEvent = (type, callback, options) => {
-  const listener = React.useRef(null);
-  const previousProps = React.useRef({ type, options });
+  const handleEvent = (event) => {
+    if (event.type === type) {
+      callback(event);
+    }
+  };
 
-  React.useEffect(() => {
-    const { type: previousType, options: previousOptions } = previousProps;
-
-    if (listener.current) {
-      window.removeEventListener(
-        previousType,
-        listener.current,
-        previousOptions
-      );
+  useEffect(() => {
+    if (options) {
+      window.addEventListener(type, handleEvent, options);
+    } else {
+      window.addEventListener(type, handleEvent);
     }
 
-    listener.current = window.addEventListener(type, callback, options);
-    previousProps.current = { type, options };
-
     return () => {
-      window.removeEventListener(type, listener.current, options);
-    };
-  }, [callback, type, options]);
-};
+      window.removeEventListener(
```

#### solution 3

```diff
--- canonical.py

+++ solution3.py

@@ -1,23 +1,15 @@

 const useOnGlobalEvent = (type, callback, options) => {
-  const listener = React.useRef(null);
-  const previousProps = React.useRef({ type, options });
+  const listener = useCallback(() => {
+    try {
+      callback();
+    } catch (error) {
+      console.error(error);
+    }
+  }, [callback]);
 
-  React.useEffect(() => {
-    const { type: previousType, options: previousOptions } = previousProps;
-
-    if (listener.current) {
-      window.removeEventListener(
-        previousType,
-        listener.current,
-        previousOptions
-      );
-    }
-
-    listener.current = window.addEventListener(type, callback, options);
-    previousProps.current = { type, options };
-
+  useEffect(() => {
+    document.addEventListener(type, listener, options);
     return () => {
-      window.removeEventListener(type, listener.current, options);
+      document.removeEventListener(type, listener, options);
     };
-  }, [callback, type, options]);
-};
+  }, [type, listener, options]);
```

#### solution 4

```diff
--- canonical.py

+++ solution4.py

@@ -1,23 +1,19 @@

 const useOnGlobalEvent = (type, callback, options) => {
-  const listener = React.useRef(null);
-  const previousProps = React.useRef({ type, options });
+  if (typeof window.addEventListener === 'undefined') {
+    return;
+  }
 
-  React.useEffect(() => {
-    const { type: previousType, options: previousOptions } = previousProps;
+  const listener = (event) => {
+    if (event.type === type) {
+      callback(event);
+    }
+  };
 
-    if (listener.current) {
-      window.removeEventListener(
-        previousType,
-        listener.current,
-        previousOptions
-      );
-    }
+  window.addEventListener(type, listener, options);
 
-    listener.current = window.addEventListener(type, callback, options);
-    previousProps.current = { type, options };
+  return () => {
+    window.removeEventListener(type, listener);
+  };
+};
 
-    return () => {
-      window.removeEventListener(type, listener.current, options);
-    };
-  }, [callback, type, options]);
-};
+export default use
```

